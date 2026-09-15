"""Single R04 execution preflight; no judging, retries, or benchmark generation.

Run with one argument: an already prepared clean-room directory containing
repo/, host/ with a CLI-installed skill, identities.json, and checks.json.
The final answer is never used to infer reference loading.
"""
import datetime
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys

base = Path(sys.argv[1]).resolve()
repo, host = base / 'repo', base / 'host'
evidence = base / 'model'
evidence.mkdir(exist_ok=False)
identity = json.loads((base / 'identities.json').read_text())
checks = json.loads((base / 'checks.json').read_text())
assert len(checks) == 7 and all(c['exit_code'] == 0 for c in checks)
assert subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=repo, text=True).strip() == identity['authoritative_head']
assert not subprocess.check_output(['git', 'status', '--porcelain'], cwd=repo, text=True)
fixture = json.loads((repo / identity['fixture_path']).read_text())
input_bytes = (repo / fixture['inputs'][0]['path']).read_bytes()
assert hashlib.sha256(input_bytes).hexdigest() == fixture['inputs'][0]['sha256']
(host / 'input.txt').write_bytes(input_bytes)
prompt = ('Use $evidence-insight for the following task, using only input.txt as evidence. '
          'Read the installed Skill and its applicable references in full through the available read tools. '
          'Do not browse, install software, upload data, modify files, or read credentials. '
          'Do not read evaluation answer files.\n\n' + fixture['prompt'])
(evidence / 'prompt.txt').write_text(prompt)
cmd = ['/opt/codex/bin/codex', 'exec', '--ignore-user-config', '--ephemeral',
       '--json', '--sandbox', 'read-only', '--skip-git-repo-check',
       '-m', 'gpt-6-astra', '-c', 'model_reasoning_effort="high"',
       '-C', str(host), '-o', str(evidence / 'final-output.txt'), prompt]
record = {
    'run_id': 'R04', 'purpose': 'Execution preflight only; not regression or A/B',
    'fixture_id': fixture['id'], 'fixture_path': identity['fixture_path'],
    'fixture_sha256': identity['fixture_sha256'], 'inputs': fixture['inputs'],
    'authoritative_head': identity['authoritative_head'],
    'runtime_sha256': identity['runtime_sha256'],
    'runtime_hash_definition': identity['runtime_hash_definition'],
    'skill_sha256': identity['source_hashes']['SKILL.md'],
    'fixture_required_references': fixture['required_references'],
    'runtime_required_references_for_this_dual_output_task': sorted(
        k for k in identity['source_hashes'] if k.startswith('references/')),
    'requested_model': 'gpt-6-astra', 'observed_model': None,
    'observed_model_version': None, 'requested_reasoning_effort': 'high',
    'observed_reasoning_effort': None,
    'host': 'Codex CLI', 'host_version': '0.154.0-alpha.3',
    'tools_requested': 'Local read/calculation only; no external evidence tools',
    'effective_tool_availability': 'Requires observation in host events',
    'sandbox_requested': 'read-only',
    'configuration': 'ignore-user-config; existing host authentication unchanged',
    'command': cmd, 'cwd': str(host), 'timeout_seconds': 60,
    'start_time': datetime.datetime.now(datetime.timezone.utc).isoformat(),
}
(evidence / 'attempt.json').write_text(json.dumps(record, indent=2, ensure_ascii=False))
with (evidence / 'stdout.jsonl').open('wb') as out, (evidence / 'stderr.txt').open('wb') as err:
    process = subprocess.Popen(cmd, stdin=subprocess.DEVNULL, stdout=out, stderr=err,
                               cwd=host, start_new_session=True)
    record['pid'] = process.pid
    record['process_started'] = True
    (evidence / 'attempt.json').write_text(json.dumps(record, indent=2, ensure_ascii=False))
    try:
        code = process.wait(timeout=60)
        record['timed_out'] = False
    except subprocess.TimeoutExpired:
        record['timed_out'] = True
        os.killpg(process.pid, signal.SIGTERM)
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            process.wait()
        code = 124
record.update(end_time=datetime.datetime.now(datetime.timezone.utc).isoformat(),
              exit_status=code, process_returncode=process.returncode,
              stdout_bytes=(evidence / 'stdout.jsonl').stat().st_size,
              stderr_bytes=(evidence / 'stderr.txt').stat().st_size,
              final_output_file_exists=(evidence / 'final-output.txt').exists())
(evidence / 'attempt.json').write_text(json.dumps(record, indent=2, ensure_ascii=False))
print(json.dumps(record, indent=2, ensure_ascii=False))
