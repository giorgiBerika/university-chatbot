from rouge_score import rouge_scorer


def evaluate( test_case, actual_result ):
    text_answer = test_case["expected_answer"]
    ai_response = actual_result["response"] 

    expected_source = test_case["expected_source"]
    actual_source = [ couple["source"] for couple in actual_result["source"] ]
    source_match = expected_source in actual_source

    scorer = rouge_scorer.RougeScorer(['rougeL'])
    scores = scorer.score(text_answer, ai_response)
    rouge_l = scores['rougeL'].fmeasure
    
    return { "rouge_l": rouge_l, "source_match": source_match }
