#!/usr/bin/env python3
"""Create blind packets and a separate mapping. Never judge or rewrite outputs."""
import argparse,hashlib,json,random,secrets
from collections import defaultdict
from pathlib import Path
from eval_core import MATCH,check_runs,read_jsonl

def blind(runs,seed):
    check_runs(runs);groups=defaultdict(list)
    for r in runs:
        groups[(r['experiment_id'],r['phase'],r['case_id'],r['run_index'])].append(r)
    rng=random.Random(seed);packets=[];mapping=[]
    for key,items in sorted(groups.items()):
        if len(items)!=2 or len({i['arm'] for i in items})!=2:raise ValueError('Each pair needs exactly two different arms')
        expected={'internal','public'} if key[1]=='migration' else {'baseline','evidence-insight'}
        if {i['arm'] for i in items}!=expected:raise ValueError('Wrong arms for phase')
        if any(items[0][m]!=items[1][m] for m in MATCH):raise ValueError('Mismatched model/input/tools/rubric/run configuration')
        if any(i['status']!='completed' for i in items):raise ValueError('Incomplete pair; retain execution error separately')
        rng.shuffle(items)
        pid=hashlib.sha256((str(seed)+repr(key)).encode()).hexdigest()[:24]
        packets.append({'pair_id':pid,'case_id':key[2],'input_sha256':items[0]['input_sha256'],
                        'A':items[0]['output'],'B':items[1]['output']})
        mapping.append({'pair_id':pid,'A':items[0]['run_id'],'B':items[1]['run_id']})
    rng.shuffle(packets)
    return packets,mapping

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--runs',type=Path,required=True)
    p.add_argument('--packets',type=Path,required=True);p.add_argument('--mapping',type=Path,required=True)
    p.add_argument('--seed',type=int);a=p.parse_args()
    if a.packets.resolve().parent==a.mapping.resolve().parent:raise SystemExit('Keep judge packets and private mapping in different directories')
    if not a.mapping.name.endswith('.private.json'):raise SystemExit('Use a .private.json mapping filename')
    packets,mapping=blind(read_jsonl(a.runs),a.seed if a.seed is not None else secrets.randbits(128))
    a.packets.parent.mkdir(parents=True,exist_ok=True);a.mapping.parent.mkdir(parents=True,exist_ok=True)
    with a.packets.open('x') as f:f.write('\n'.join(json.dumps(x,ensure_ascii=False) for x in packets)+'\n')
    with a.mapping.open('x') as f:json.dump(mapping,f,ensure_ascii=False,indent=2)
    a.mapping.chmod(0o600)
    print(f'{len(packets)} blinded pairs. Mapping is private; do not give it to a judge.')
if __name__=='__main__':main()
