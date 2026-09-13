"""Deterministic engine checks. Test records stay in memory, not results/."""
import copy,hashlib,json,sys,tempfile,unittest,zipfile
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from eval_core import ROOT,HARD,QUALITY,aggregate,aggregate_preferences,check_runs
from prepare_blind_eval import blind
from build_report import render
from build_chatgpt_bundle import build
from validate import migration_checks,skill_checks,yaml_unique

def run(arm='baseline',index=1):
    output='Test-only synthetic output. Never a model benchmark record.'
    return dict(record_type='run',record_kind='actual',schema_version='1.0.0',experiment_id='unit-test-only',phase='ab',
      run_id=arm+str(index),case_id='R01',split='regression',arm=arm,model='test-double',model_version=None,reasoning_effort='test',
      date='2026-01-01T00:00:00Z',host_version='test',tool_availability=['read-fixture'],tool_budget='none',context_mode='frozen-inputs',
      input_sha256='a'*64,runtime_sha256=None if arm=='baseline' else 'b'*64,rubric_version='1.0.0',declared_runs=3,run_index=index,
      status='completed',output=output,output_sha256=hashlib.sha256(output.encode()).hexdigest(),tool_trace_available=True,trace_path='test-only',error=None)

def judgment(r):
    return dict(record_type='judgment',run_id=r['run_id'],judge_id='test-human',judge_kind='human',judge_version='unit-test',rubric_version='1.0.0',
      blinded=True,adjudicated=True,output_sha256=r['output_sha256'],hard={m:('pass' if m in ['causal_overclaim','evidence_applicability_error'] else 'N/A') for m in HARD},quality={m:None for m in QUALITY},
      evidence=[dict(metric='factual_fabrication',output_excerpt='',reason='Unit test only',source_reference='test fixture')])

class Engineering(unittest.TestCase):
    def test_original_line_coverage(self):self.assertGreater(migration_checks(ROOT),2000)
    def test_standalone_runtime(self):
        import shutil
        with tempfile.TemporaryDirectory() as t:
            path=Path(t)/'evidence-insight';shutil.copytree(ROOT/'skills/evidence-insight',path)
            self.assertEqual(skill_checks(path)['runtime_references'],10)
            (path/'references/semantic-strength.md').unlink()
            with self.assertRaises(ValueError):skill_checks(path)
    def test_duplicate_yaml_rejected(self):
        with self.assertRaises(ValueError):yaml_unique('name: a\nname: b\n')
    def test_empty_report_is_pending(self):
        result=aggregate([],[]);self.assertEqual(result['groups'],[])
        self.assertIn('Results pending.',render(result));self.assertNotIn('100%',render(result))
    def test_duplicate_and_synthetic_runs_rejected(self):
        r=run()
        with self.assertRaises(ValueError):check_runs([r,r])
        r['record_kind']='synthetic'
        with self.assertRaises(Exception):check_runs([r])
    def test_output_tampering_rejected(self):
        r=run();r['output']='changed'
        with self.assertRaises(ValueError):check_runs([r])
    def test_missing_and_unscorable_are_not_passes(self):
        a,b=run(),run('evidence-insight');j=judgment(a)
        j['hard']['factual_fabrication']='unscorable'
        result=aggregate([a,b],[j]);self.assertEqual(result['adjudicated_runs'],1)
        self.assertEqual(sum(g['unjudged'] for g in result['groups']),1)
        self.assertEqual(result['groups'][0]['hard']['factual_fabrication'].get('pass',0),0)
    def test_injection_needs_trace(self):
        r=run();r['tool_trace_available']=False;j=judgment(r)
        j['hard']['prompt_injection_compliance_failure']='pass'
        with self.assertRaises(ValueError):aggregate([r],[j])
    def test_incomplete_cannot_be_scored(self):
        r=run();r['status']='error';j=judgment(r)
        with self.assertRaises(ValueError):aggregate([r],[j])
    def test_blind_packet_hides_arms(self):
        runs=[run(),run('evidence-insight')];packets,mapping=blind(runs,42)
        self.assertEqual(set(packets[0]),{'pair_id','case_id','input_sha256','A','B'})
        self.assertNotIn('baseline',json.dumps(packets));self.assertNotIn('evidence-insight',json.dumps(packets))
        self.assertEqual({mapping[0]['A'],mapping[0]['B']},{r['run_id'] for r in runs})
        self.assertEqual(blind(runs,42),(packets,mapping))
    def test_mismatched_comparison_rejected(self):
        a,b=run(),run('evidence-insight');b['reasoning_effort']='different'
        with self.assertRaises(ValueError):blind([a,b],0)
    def test_preference_resolves_blind_labels(self):
        runs=[run(),run('evidence-insight')];packets,mapping=blind(runs,42)
        pref=dict(record_type='preference',pair_id=packets[0]['pair_id'],judge_id='test',judge_kind='human',judge_version='unit-test',rubric_version='1.0.0',blinded=True,adjudicated=True,
                  choice='A',reason='Synthetic test only',A_sha256=runs[0]['output_sha256'],B_sha256=runs[1]['output_sha256'])
        result=aggregate_preferences(runs,[pref],mapping)
        winner=next(r['arm'] for r in runs if r['run_id']==mapping[0]['A'])
        self.assertEqual(result[0]['choices'][winner],1)
        with self.assertRaises(ValueError):aggregate_preferences(runs,[pref,pref],mapping)
    def test_double_adjudication_rejected(self):
        r=run();a=judgment(r);b=copy.deepcopy(a);b['judge_id']='another'
        with self.assertRaises(ValueError):aggregate([r],[a,b])
    def test_bundle_has_every_reference_and_license(self):
        with tempfile.TemporaryDirectory() as t:
            p=build(Path(t))
            with zipfile.ZipFile(p) as z:
                text=z.read('evidence-insight-runtime-1.0.0.md').decode()
                manifest=json.loads(z.read('bundle-manifest.json'))
                self.assertEqual(len(manifest['source_hashes']),11)
                for ref in (ROOT/'skills/evidence-insight/references').glob('*.md'):
                    self.assertIn(ref.read_text(),text)
                self.assertEqual(z.read('LICENSE'),(ROOT/'LICENSE').read_bytes())
    def test_dataset_missing_values_and_unit_conversion(self):
        import csv
        with (ROOT/'evals/cases/inputs/amounts.csv').open() as f:
            values=[int(r['amount_cents']) for r in csv.DictReader(f)]
        self.assertEqual(sum(x for x in values if x!=-1),350)
    def test_archive_fixture_is_inert(self):
        with zipfile.ZipFile(ROOT/'evals/cases/inputs/I03.zip') as z:
            self.assertEqual(set(z.namelist()),{'README.txt','data.csv'})
            self.assertEqual(z.read('data.csv'),b'value\n7\n')

if __name__=='__main__':unittest.main()
