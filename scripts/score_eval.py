#!/usr/bin/env python3
"""Validate and aggregate recorded human/model judgments. Does not judge text."""
import argparse,json
from pathlib import Path
from eval_core import aggregate,aggregate_preferences,read_jsonl

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--runs',type=Path,required=True);p.add_argument('--judgments',type=Path,required=True)
    p.add_argument('--preferences',type=Path);p.add_argument('--mapping',type=Path)
    a=p.parse_args()
    if bool(a.preferences)!=bool(a.mapping):p.error('preferences and private mapping must be supplied together, after judging is locked')
    runs=read_jsonl(a.runs);result=aggregate(runs,read_jsonl(a.judgments))
    if a.preferences:result['direct_post_preference']=aggregate_preferences(runs,read_jsonl(a.preferences),json.loads(a.mapping.read_text()))
    print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
