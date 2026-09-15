#!/usr/bin/env python3
"""Bundle the single public runtime for manual ChatGPT Project upload."""
import argparse,hashlib,json,re,zipfile
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]
def build(out):
    skill=ROOT/'skills/evidence-insight';body=(skill/'SKILL.md').read_text()
    version=yaml.safe_load(body.split('---',2)[1])['metadata']['version']
    adapter=(ROOT/'adapters/chatgpt-project-instructions.txt').read_text()
    if f'【当前项目指示版本：{version}】' not in adapter:raise ValueError('Adapter version mismatch')
    refs=re.findall(r'\]\((references/[^)]+\.md)\)',body)
    if len(set(refs))!=len(list((skill/'references').glob('*.md'))):raise ValueError('Unlinked or duplicate references')
    # Explicit same-document anchors replace paths that do not exist in a Project upload.
    for ref in refs:body=body.replace('('+ref+')','(#'+Path(ref).stem+')')
    chunks=[f'# Evidence Insight runtime {version}', '',
      'The entrypoint and every reference follow in this one document. Reference-loading conditions identify the relevant sections; no separate file lookup is needed.', '', body]
    hashes={'SKILL.md':hashlib.sha256((skill/'SKILL.md').read_bytes()).hexdigest()}
    for ref in refs:
        chunks += ['',f'<a id="{Path(ref).stem}"></a>',(skill/ref).read_text()]
        hashes[ref]=hashlib.sha256((skill/ref).read_bytes()).hexdigest()
    out.mkdir(parents=True,exist_ok=True)
    name=f'evidence-insight-chatgpt-{version}.zip'
    with zipfile.ZipFile(out/name,'w',compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr(f'evidence-insight-runtime-{version}.md','\n'.join(chunks))
        z.writestr('chatgpt-project-instructions.txt',adapter)
        z.writestr('LICENSE',(ROOT/'LICENSE').read_text())
        z.writestr('bundle-manifest.json',json.dumps({'version':version,'source_hashes':hashes,'host_behavior':'UNVERIFIED'},indent=2))
    return out/name
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,default=ROOT/'dist');a=p.parse_args();print(build(a.output))
