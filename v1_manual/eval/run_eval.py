import json
from pathlib import Path 
import sys 

root =  Path(__file__).parent.parent 
sys.path.insert(0, str(root))

from v1_manual.pipeline.qa import run_query
from v1_manual.eval.evaluator import evaluate

with open('eval/test_cases.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


for test in data:

    question = test["question"]
    ai_response = run_query(question)

    result = evaluate( test, ai_response )

    print(f"{result}\n")
     
