from retrieval.search import search_in_db 
from generation.llm import llm_response 

def run_query( question ):
    search_results = search_in_db(question)

    response = llm_response( search_results, question)

    return response 