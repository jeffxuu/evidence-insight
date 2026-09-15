#!/usr/bin/env python3
"""Render a report from validated actual runs and adjudications, never placeholders."""
import argparse,json
from pathlib import Path
from eval_core import aggregate,aggregate_preferences,read_jsonl

def render(report):
    lines=['# Evaluation report','','Benchmark methodology available.',report['status'],'',report['note'],'']
    if not report['groups']:return '\n'.join(lines)+'\n'
    lines += ['| Experiment / phase / split / arm | Executions | Completed | Errors | Adjudicated | Unjudged | Any hard failure |',
              '| --- | ---: | ---: | ---: | ---: | ---: | ---: |']
    for g in report['groups']:
        label=' / '.join(g[k] for k in ['experiment_id','phase','split','arm'])
        lines.append(f'| {label} | {g["executions"]} | {g["completed"]} | {g["execution_errors"]} | {g["judged"]} | {g["unjudged"]} | {g["any_hard_failure"]} |')
    for g in report['groups']:
        label=' / '.join(g[k] for k in ['experiment_id','phase','split','arm'])
        lines.extend(['',f'## {label}','','| Hard metric | Pass | Fail | N/A | Unscorable |','| --- | ---: | ---: | ---: | ---: |'])
        for m,c in g['hard'].items():lines.append(f'| {m} | {c.get("pass",0)} | {c.get("fail",0)} | {c.get("N/A",0)} | {c.get("unscorable",0)} |')
        lines += ['','| Quality metric | 0 | 1 | 2 | 3 | 4 | N/A |','| --- | ---: | ---: | ---: | ---: | ---: | ---: |']
        for m,c in g['quality'].items():lines.append('| '+m+' | '+' | '.join(str(c.get(k,0)) for k in ['0','1','2','3','4','N/A'])+' |')
    if report.get('direct_post_preference'):
        lines += ['','## Direct-post preference','','Randomized labels resolved after judging. Counts only; ties and neither retained.','']
        for group in report['direct_post_preference']:
            lines.append('- '+group['experiment_id']+' / '+group['phase']+' / '+group['split']+': '+json.dumps(group['choices'],ensure_ascii=False))
    return '\n'.join(lines)+'\n'

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--runs',type=Path,required=True);p.add_argument('--judgments',type=Path,required=True)
    p.add_argument('--preferences',type=Path);p.add_argument('--mapping',type=Path);a=p.parse_args()
    if bool(a.preferences)!=bool(a.mapping):p.error('preferences and mapping are required together')
    runs=read_jsonl(a.runs);result=aggregate(runs,read_jsonl(a.judgments))
    if a.preferences:result['direct_post_preference']=aggregate_preferences(runs,read_jsonl(a.preferences),json.loads(a.mapping.read_text()))
    print(render(result),end='')
if __name__=='__main__':main()
