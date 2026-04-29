import ollama
from v1_manual.config import LLM


def llm_response( search_res, user_question ):
    system_prompt = """ 

        You are a helpful university assistant.
        Answer questions only based on the provided
        context. If the answer is not in the context,
        say you don't know.    

        """


    search_text = search_res["documents"]

    cont = f"Based only on the given information: {search_text}, answer this question: {user_question}"

    response = ollama.chat (
            model=LLM,
            messages=[
                { "role" :"system", "content": system_prompt },
                { "role":"user", "content": cont } 
            ]
    )

    return response.message.content
