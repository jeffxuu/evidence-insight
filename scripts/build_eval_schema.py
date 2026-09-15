#!/usr/bin/env python3
"""Regenerate the evaluation JSON schema from the documented record contract."""
import json
from eval_core import ROOT,HARD,QUALITY

def main():
    def string():return {'type':'string','minLength':1}
    sha={'type':'string','pattern':'^[0-9a-f]{64}$'}
    def obj(props):return {'type':'object','properties':props,'required':list(props),'additionalProperties':False}
    def array(items):return {'type':'array','items':items}
    case=obj({'schema_version':{'const':'1.0.0'},'id':string(),'split':{'enum':['regression','public-challenge','holdout']},'category':string(),'title':string(),'origin':string(),'license':string(),'prompt':string(),
      'inputs':dict(array(obj({'path':string(),'sha256':sha})),minItems=1),
      'expected_boundaries':dict(array(string()),minItems=1),'hard_metrics':dict(array({'enum':HARD}),minItems=1,uniqueItems=True),
      'required_references':array(string()),'execution_status':{'const':'not_run'},'external_tools':string()})
    run=obj({'record_type':{'const':'run'},'record_kind':{'const':'actual'},'schema_version':{'const':'1.0.0'},'experiment_id':string(),'phase':{'enum':['migration','ab']},'run_id':string(),'case_id':string(),
      'split':{'enum':['regression','public-challenge','holdout']},'arm':{'enum':['internal','public','baseline','evidence-insight']},'model':string(),'model_version':{'type':['string','null']},'reasoning_effort':string(),
      'date':{'type':'string','format':'date-time'},'host_version':string(),'tool_availability':array(string()),'tool_budget':string(),'context_mode':{'enum':['frozen-inputs','live-web']},'input_sha256':sha,
      'runtime_sha256':{'type':['string','null'],'pattern':'^[0-9a-f]{64}$'},'rubric_version':{'const':'1.0.0'},'declared_runs':{'type':'integer','minimum':3},'run_index':{'type':'integer','minimum':1},
      'status':{'enum':['completed','error','timeout','tool_unavailable']},'output':{'type':'string'},'output_sha256':sha,'tool_trace_available':{'type':'boolean'},'trace_path':{'type':['string','null']},'error':{'type':['string','null']}})
    judgment=obj({'record_type':{'const':'judgment'},'run_id':string(),'judge_id':string(),'judge_kind':{'enum':['human','independent-model']},'judge_version':string(),'rubric_version':{'const':'1.0.0'},
      'blinded':{'const':True},'adjudicated':{'type':'boolean'},'output_sha256':sha,
      'hard':obj({m:{'enum':['pass','fail','N/A','unscorable']} for m in HARD}),
      'quality':obj({m:{'type':['integer','null'],'minimum':0,'maximum':4} for m in QUALITY}),
      'evidence':dict(array(obj({'metric':{'enum':HARD+QUALITY},'output_excerpt':{'type':'string'},'reason':string(),'source_reference':string()})),minItems=1)})
    preference=obj({'record_type':{'const':'preference'},'pair_id':string(),'judge_id':string(),'judge_kind':{'enum':['human','independent-model']},'judge_version':string(),
      'rubric_version':{'const':'1.0.0'},'blinded':{'const':True},'adjudicated':{'type':'boolean'},'choice':{'enum':['A','B','Tie','Neither']},'reason':string(),'A_sha256':sha,'B_sha256':sha})
    (ROOT/'evals/schema.json').write_text(json.dumps({'$schema':'https://json-schema.org/draft/2020-12/schema','title':'Evidence Insight evaluation records 1.0.0','$defs':{'case':case,'run':run,'judgment':judgment,'preference':preference}},indent=2)+'\n')
if __name__=='__main__':main()
