#!/usr/bin/env python3
"""Validate packaging, source-line migration, schemas, links and material hygiene.

This is deterministic engineering validation, not an LLM behavioral benchmark.
"""
import argparse,hashlib,json,re
from pathlib import Path
from urllib.parse import unquote,urlsplit
import yaml
from markdown_it import MarkdownIt
from skills_ref.validator import validate as official_validate
from eval_core import ROOT,validate_record

def inside(root,path):
    path=path.resolve()
    if not path.is_relative_to(root.resolve()):raise ValueError(f'Path escapes allowed directory: {path}')
    return path

def yaml_unique(text):
    class Loader(yaml.SafeLoader):pass
    def mapping(loader,node,deep=False):
        keys=[loader.construct_object(k,deep=deep) for k,_ in node.value]
        if len(keys)!=len(set(keys)):raise ValueError('Duplicate YAML keys')
        return yaml.SafeLoader.construct_mapping(loader,node,deep)
    Loader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,mapping)
    return yaml.load(text,Loader=Loader)

def skill_checks(skill):
    errors=official_validate(skill)
    if errors:raise ValueError('; '.join(errors))
    text=(skill/'SKILL.md').read_text();meta=yaml_unique(text.split('---',2)[1])
    if meta.get('metadata',{}).get('version')!='1.0.0':raise ValueError('Public version must be string 1.0.0')
    if meta.get('license')!='Apache-2.0':raise ValueError('License mismatch')
    if any(not isinstance(k,str) or not isinstance(v,str) for k,v in meta['metadata'].items()):raise ValueError('metadata keys/values must be strings')
    refs=re.findall(r'\]\((references/[^)]+\.md)\)',text)
    for ref in refs:
        p=inside(skill,skill/ref)
        if not p.is_file():raise ValueError('Missing runtime reference '+ref)
    actual={str(p.relative_to(skill)) for p in (skill/'references').glob('*.md')}
    if set(refs)!=actual or len(refs)!=len(actual):raise ValueError('Every reference must appear exactly once in root loading table')
    for p in [skill/'SKILL.md',*(skill/'references').glob('*.md')]:
        s=p.read_text()
        if re.search(r'V7(?:\.\d+)*|7\.6\.3|Image Insight|SKILL_V',s):raise ValueError('Internal lineage in public runtime '+str(p))
        for match in re.finditer(r'\]\(([^)]+)\)',s):
            href=match.group(1)
            if not urlsplit(href).scheme and not href.startswith('#'):
                inside(skill,skill/href)
    if not (skill/'LICENSE').is_file():raise ValueError('Standalone skill license missing')
    return {'official_spec':'VERIFIED','runtime_references':len(refs),'entrypoint_lines':len(text.splitlines()),'behavior':'UNVERIFIED'}

def migration_checks(root):
    data=json.loads((root/'docs/migration/manifest.json').read_text());rows=data['rules'];seen=set();sources={}
    for row in rows:
        key=(row['source'],row['source_line'])
        if key in seen:raise ValueError('Duplicate migration source line')
        seen.add(key)
        src=inside(root,root/row['source']);dst=inside(root,root/row['destination'])
        a=sources.setdefault(row['source'],src.read_text().splitlines())
        b=dst.read_text().splitlines()
        if a[row['source_line']-1]!=row['source_text']:raise ValueError('Source manifest mismatch '+row['id'])
        if b[row['destination_line']-1]!=row['destination_text']:raise ValueError('Destination manifest mismatch '+row['id'])
        if not row['original_trigger'] or not row['new_loading_condition'] or not row['regression']:raise ValueError('Missing trigger/loading/regression mapping')
        for case in row['regression']:
            if not (root/f'evals/regression/{case}.json').is_file():raise ValueError('Missing regression '+case)
        if row['destination'].startswith('skills/evidence-insight/references/'):
            name=dst.name;condition=data['reference_load_conditions'][name]
            main=(root/'skills/evidence-insight/SKILL.md').read_text()
            if condition!=row['new_loading_condition'] or condition not in main:raise ValueError('Loading condition not reachable from SKILL.md')
        if row['source_text']!=row['destination_text'] and row['change_type']==['verbatim-move']:raise ValueError('Unrecorded change')
    expected={(str(p.relative_to(root)),n) for p in (root/'docs/migration/internal').iterdir() if p.is_file() for n,t in enumerate(p.read_text().splitlines(),1) if t.strip()}
    if seen!=expected:raise ValueError(f'Migration coverage gap: {len(expected-seen)} missing, {len(seen-expected)} extra')
    raw=root/'docs/migration/internal/SKILL_V7.6.3.md'
    if hashlib.sha256(raw.read_bytes()).hexdigest()!=data['source_sha256']:raise ValueError('Source fingerprint mismatch')
    security_lines=set()
    for row in data['approved_additions']:
        target=inside(root,root/row['destination'])
        if target.read_text().splitlines()[row['destination_line']-1]!=row['destination_text']:raise ValueError('Security addition mismatch')
        if row['new_loading_condition']!=data['reference_load_conditions']['security-boundary.md']:raise ValueError('Security loading mismatch')
        security_lines.add(row['destination_line'])
    expected_security={i for i,line in enumerate((root/'skills/evidence-insight/references/security-boundary.md').read_text().splitlines(),1) if line.strip()}
    if security_lines!=expected_security:raise ValueError('Security addition coverage gap')
    return len(rows)

def markdown_checks(root):
    parser=MarkdownIt('commonmark',{'html':True}).enable('table')
    count=0
    for p in root.rglob('*.md'):
        rel=p.relative_to(root)
        if any(x in rel.parts for x in ['.git','node_modules','dist','__pycache__']):continue
        text=p.read_text();tokens=parser.parse(text);count+=1
        for token in tokens:
            for child in token.children or []:
                href=child.attrGet('href') if child.type=='link_open' else child.attrGet('src') if child.type=='image' else None
                if not href or urlsplit(href).scheme:continue
                path,_,anchor=href.partition('#')
                target=inside(root,p.parent/unquote(path)) if path else p
                if not target.exists():raise ValueError(f'Broken Markdown reference: {rel}: {href}')
                if anchor and target.suffix=='.md':
                    body=target.read_text()
                    anchors=set(re.findall(r'<a\s+id="([^"]+)"',body))
                    for heading in re.findall(r'^#{1,6}\s+(.+)$',body,re.M):
                        anchors.add(re.sub(r'[^\w\- ]','',heading.lower()).replace(' ','-'))
                    if unquote(anchor) not in anchors:raise ValueError(f'Unknown heading: {rel}: {href}')
        fences=re.findall(r'^(`{3,}|~{3,})',text,re.M)
        if len(fences)%2:raise ValueError('Unclosed Markdown fence '+str(rel))
    return count

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--skill-only',type=Path);a=p.parse_args()
    if a.skill_only:
        print(json.dumps(skill_checks(a.skill_only.resolve()),indent=2));return
    root=ROOT;report=skill_checks(root/'skills/evidence-insight')
    report['migration_source_lines']=migration_checks(root)
    adapter=(root/'adapters/chatgpt-project-instructions.txt').read_text()
    if '【当前项目指示版本：1.0.0】' not in adapter or '【对应 Skill：evidence-insight 1.0.0】' not in adapter:raise ValueError('Adapter version mismatch')
    if (root/'LICENSE').read_bytes()!=(root/'skills/evidence-insight/LICENSE').read_bytes():raise ValueError('License copies differ')
    cases=list((root/'evals/regression').glob('*.json'))
    for path in cases:
        case=json.loads(path.read_text());validate_record(case,'case')
        for inp in case['inputs']:
            q=inside(root,root/inp['path'])
            if hashlib.sha256(q.read_bytes()).hexdigest()!=inp['sha256']:raise ValueError('Fixture hash mismatch '+inp['path'])
        for ref in case['required_references']:
            if not (root/'skills/evidence-insight/references'/ref).is_file():raise ValueError('Unknown reference in case')
    for p in (root/'.github').rglob('*.yml'):yaml_unique(p.read_text())
    report['markdown_files']=markdown_checks(root)
    report['public_regression_cases']=len(cases)
    patterns=[r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',r'\b(?:ghp|github_pat)_[A-Za-z0-9_]{20,}',r'\bsk-[A-Za-z0-9_-]{20,}']
    for path in root.rglob('*'):
        if not path.is_file() or any(x in path.relative_to(root).parts for x in ['.git','node_modules','dist','__pycache__']):continue
        if path.is_symlink():raise ValueError('Review symlink before public distribution '+str(path))
        if path.suffix in ['.png','.zip','.pyc']:continue
        text=path.read_text()
        if any(re.search(x,text) for x in patterns):raise ValueError('Potential secret in '+str(path.relative_to(root)))
    report['secret_pattern_scan']='VERIFIED (limited patterns; not a complete secrecy guarantee)'
    report['copyright_provenance']='PARTIALLY VERIFIED; see materials review'
    print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
