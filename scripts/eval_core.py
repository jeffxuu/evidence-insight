"""Shared validation for actual evaluation records; no model judging is implied."""
from pathlib import Path
import hashlib
import json
from collections import Counter
import jsonschema

ROOT=Path(__file__).resolve().parents[1]
HARD=['factual_fabrication','claim_source_mismatch','causal_overclaim','qualifier_loss',
      'semantic_strength_violation','evidence_applicability_error','artifact_leakage','prompt_injection_compliance_failure']
QUALITY=['information_gain','explanatory_leverage','source_relevance','analysis_focus','thesis_clarity','authorial_ownership','social_direct_post_readiness']
MATCH=['model','model_version','reasoning_effort','tool_availability','input_sha256','rubric_version','declared_runs','context_mode','host_version','tool_budget']

def read_jsonl(path):
    return [json.loads(x) for x in Path(path).read_text().splitlines() if x.strip()]

def validate_record(record,kind):
    schema=json.loads((ROOT/'evals/schema.json').read_text())
    jsonschema.Draft202012Validator({'$ref':f'#/$defs/{kind}','$defs':schema['$defs']},format_checker=jsonschema.FormatChecker()).validate(record)

def check_runs(runs):
    seen=set();slots=set()
    for r in runs:
        validate_record(r,'run')
        if r['run_id'] in seen: raise ValueError('Duplicate run_id')
        seen.add(r['run_id'])
        slot=tuple(r[k] for k in ['experiment_id','phase','case_id','arm','run_index'])
        if slot in slots:raise ValueError('Duplicate case/arm/run-index slot')
        slots.add(slot)
        if r['run_index']>r['declared_runs']:raise ValueError('Run index exceeds declared run count')
        allowed={'internal','public'} if r['phase']=='migration' else {'baseline','evidence-insight'}
        if r['arm'] not in allowed:raise ValueError('Arm does not match phase')
        if r['record_kind']!='actual': raise ValueError('Only actual executions can enter evaluation reports')
        if r['status']=='completed' and not r['output'].strip(): raise ValueError('Completed run has empty output')
        if r['output_sha256']!=hashlib.sha256(r['output'].encode()).hexdigest(): raise ValueError('Output hash mismatch')

def aggregate(runs,judgments):
    check_runs(runs)
    run_map={r['run_id']:r for r in runs};by_run={};seen=set()
    for j in judgments:
        validate_record(j,'judgment')
        key=(j['run_id'],j['judge_id'])
        if key in seen: raise ValueError('Duplicate judgment by the same judge')
        seen.add(key)
        if j['run_id'] not in run_map: raise ValueError('Judgment references unknown run')
        r=run_map[j['run_id']]
        if r['status']!='completed': raise ValueError('Cannot score an incomplete run as completed')
        if j['rubric_version']!=r['rubric_version']: raise ValueError('Rubric mismatch')
        if j['output_sha256']!=r['output_sha256']: raise ValueError('Judgment output hash mismatch')
        if not j['blinded']: raise ValueError('Unblinded judgments are excluded from benchmark reports')
        case_file=ROOT/'evals/regression'/f'{r["case_id"]}.json'
        if case_file.is_file():
            case=json.loads(case_file.read_text())
            if any(j['hard'][m]=='N/A' for m in case['hard_metrics']):raise ValueError('Predeclared applicable hard metric cannot be N/A')
        explained={e['metric'] for e in j['evidence']}
        needs={m for m,v in j['hard'].items() if v in {'fail','unscorable'}} | {m for m,v in j['quality'].items() if v is not None and v<4}
        if not needs.issubset(explained):raise ValueError('Missing rubric evidence for defect/nonmaximum quality score')
        if j['hard']['prompt_injection_compliance_failure']=='pass' and not r['tool_trace_available']:
            raise ValueError('Injection pass requires a tool trace, not only final text')
        if j['adjudicated']:
            if j['run_id'] in by_run: raise ValueError('Multiple final adjudications for one run')
            by_run[j['run_id']]=j
    groups={}
    for r in runs:
        key=(r['experiment_id'],r['phase'],r['split'],r['arm'])
        g=groups.setdefault(key,{'experiment_id':key[0],'phase':key[1],'split':key[2],'arm':key[3],
            'executions':0,'completed':0,'execution_errors':0,'unjudged':0,'judged':0,
            'any_hard_failure':0,'hard':{m:Counter() for m in HARD},'quality':{m:Counter() for m in QUALITY}})
        g['executions']+=1
        if r['status']!='completed':g['execution_errors']+=1;continue
        g['completed']+=1
        if r['run_id'] not in by_run:g['unjudged']+=1;continue
        j=by_run[r['run_id']];g['judged']+=1
        g['any_hard_failure']+=int('fail' in j['hard'].values())
        for m,v in j['hard'].items():g['hard'][m][v]+=1
        for m,v in j['quality'].items():g['quality'][m]['N/A' if v is None else str(v)]+=1
    return {'report_version':'1.0.0','status':'Results pending.' if not runs else 'Recorded executions; judge coverage shown separately.',
            'groups':list(groups.values()),'runs':len(runs),'adjudicated_runs':len(by_run),
            'note':'Counts only. No subjective total, improvement claim or independence assumption. Unscorable and N/A are not passes.'}

def aggregate_preferences(runs,preferences,mapping):
    check_runs(runs);runmap={r['run_id']:r for r in runs};pairs={};seen=set();result={}
    for p in mapping:
        if p['pair_id'] in pairs:raise ValueError('Duplicate blind pair mapping')
        a,b=runmap[p['A']],runmap[p['B']]
        if a['arm']==b['arm'] or any(a[k]!=b[k] for k in MATCH+['experiment_id','phase','split','case_id','run_index']):raise ValueError('Invalid preference comparison')
        pairs[p['pair_id']]=p
    for pref in preferences:
        validate_record(pref,'preference')
        if not pref['adjudicated']:continue
        if pref['pair_id'] in seen:raise ValueError('Multiple final preferences for one pair')
        seen.add(pref['pair_id']);p=pairs[pref['pair_id']];a,b=runmap[p['A']],runmap[p['B']]
        if a['status']!='completed' or b['status']!='completed':raise ValueError('Preference on incomplete pair')
        if pref['A_sha256']!=a['output_sha256'] or pref['B_sha256']!=b['output_sha256']:raise ValueError('Preference output hash mismatch')
        key=(a['experiment_id'],a['phase'],a['split'])
        g=result.setdefault(key,{'experiment_id':key[0],'phase':key[1],'split':key[2],'pairs':0,'choices':Counter()})
        choice=pref['choice'];g['pairs']+=1
        # Resolve randomized labels only after judgments are locked.
        winner=runmap[p[choice]]['arm'] if choice in ['A','B'] else choice
        g['choices'][winner]+=1
    return list(result.values())
