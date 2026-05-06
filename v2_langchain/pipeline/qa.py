from pathlib import Path                                                             
import sys
sys.path.insert(0, str(Path(__file__).parent.parent)) 
from v2_langchain.vector_store import get_retriever
from v2_langchain.generation.llm import call_ai


def run_query(question):

    context = get_retriever().invoke(question)
    context_text = " ".join([ m.page_content for m in context])
    result = call_ai(context_text, question)

    return result
