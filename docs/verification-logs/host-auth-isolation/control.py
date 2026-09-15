"""One authorized bare-host control, with unchanged authentication and routing.

Usage: python control.py A-corrected|B|services
No automatic retry and no Evidence Insight input. Global configuration is read,
never rewritten; managed policy remains active. Each output directory is unique.
"""
import datetime, hashlib, json, os, signal, subprocess, sys, tempfile, threading, time, tomllib
from pathlib import Path

base = Path(__file__).resolve().parent
label = sys.argv[1]
assert label in ('A-corrected', 'B', 'services')
outdir = base / ('control-' + label)
outdir.mkdir(exist_ok=False)
host = Path(tempfile.mkdtemp(prefix='evidence-host-auth-control-'))
home = Path(os.environ.get('CODEX_HOME', str(Path.home() / '.codex')))
config = tomllib.loads((home / 'config.toml').read_text())
model = 'gpt-5.6-sol' if label == 'B' else 'gpt-6-astra'
expected = 'CODEX_HOST_OK' if label == 'B' else 'ASTRA_HOST_OK'
prompt = 'Return exactly:\n' + expected
settings = ['model_reasoning_effort="low"', 'project_doc_max_bytes=0', 'web_search="disabled"']
skills = sorted({str(f) for root in [home / 'skills', Path.home() / '.agents/skills']
                 if root.exists() for f in root.rglob('SKILL.md')})
settings.append('skills.config=[' + ','.join('{path=' + json.dumps(s) + ',enabled=false}' for s in skills) + ']')
if label != 'services':
    for name in config.get('mcp_servers', {}):
        assert name.replace('_','').replace('-','').isalnum()
        settings.append('mcp_servers.' + name + '.enabled=false')
    for name in ['apps', 'plugins', 'remote_plugin', 'code_mode_host', 'shell_tool',
                 'unified_exec', 'view_image', 'browser_use', 'computer_use', 'image_generation']:
        settings.append('features.' + name + '=false')
cmd = ['/opt/codex/bin/codex', 'exec', '--ephemeral', '--json', '--sandbox', 'read-only',
       '--skip-git-repo-check', '-m', model, '-C', str(host), '-o', str(outdir / 'final.txt')]
for s in settings:
    cmd += ['-c', s]
cmd.append(prompt)
now = lambda: datetime.datetime.now(datetime.timezone.utc).isoformat()
record = {'control': label, 'model_requested': model, 'reasoning_effort_requested': 'low',
          'authentication_path': 'existing ChatGPT file-backed auth; unchanged',
          'account_workspace': 'not exposed; credential contents not inspected',
          'configuration': 'normal user configuration and existing routing retained; per-process overrides only',
          'global_config_sha256_before': hashlib.sha256((home / 'config.toml').read_bytes()).hexdigest(),
          'command': cmd, 'start_time': now(), 'timeout_seconds': 60,
          'prompt': prompt, 'cwd': str(host), 'workspace_initial_files': list(host.iterdir()),
          'environment_values_logged': False, 'skill_inputs': [], 'fixture': None}
events = []
def capture(stream, path, kind):
    with path.open('wb') as f:
        for line in iter(stream.readline, b''):
            f.write(line); f.flush()
            events.append({'received_at': now(), 'stream': kind, 'line': line.decode(errors='replace')})
started = time.monotonic()
p = subprocess.Popen(cmd, cwd=host, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                     stderr=subprocess.PIPE, start_new_session=True)
record.update(process_started=True, pid=p.pid)
(outdir / 'attempt.json').write_text(json.dumps(record, indent=2))
threads = [threading.Thread(target=capture, args=(p.stdout,outdir/'stdout.jsonl','stdout')),
           threading.Thread(target=capture, args=(p.stderr,outdir/'stderr.txt','stderr'))]
for t in threads:t.start()
try:
    p.wait(timeout=max(0.1,60-(time.monotonic()-started)))
    code=p.returncode; timed_out=False
except subprocess.TimeoutExpired:
    timed_out=True; os.killpg(p.pid,signal.SIGTERM)
    try:p.wait(timeout=3)
    except subprocess.TimeoutExpired:os.killpg(p.pid,signal.SIGKILL);p.wait()
    code=124
for t in threads:t.join(timeout=3)
record.update(end_time=now(),elapsed_monotonic_seconds=time.monotonic()-started,
              exit_code=code,process_returncode=p.returncode,timed_out=timed_out,
              global_config_sha256_after=hashlib.sha256((home/'config.toml').read_bytes()).hexdigest(),
              final_text=(outdir/'final.txt').read_text() if (outdir/'final.txt').exists() else None)
record['exact_final_match'] = record['final_text'] is not None and record['final_text'].strip()==expected
(outdir/'attempt.json').write_text(json.dumps(record,indent=2))
(outdir/'received-events.json').write_text(json.dumps(events,indent=2))
print(json.dumps({k:record[k] for k in ['control','model_requested','start_time','end_time','exit_code','timed_out','final_text','exact_final_match']},indent=2))
