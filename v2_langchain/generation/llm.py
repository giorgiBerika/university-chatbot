from langchain_ollama import ChatOllama 
from langchain_core.prompts import ChatPromptTemplate
from config import LLM


def call_ai(context, question):
    system_prompt = """You are a helpful university assistant.
        Answer questions only based on the provided
        context. If the answer is not in the context,
        say you don't know."""
    
    model = ChatOllama(
        model=LLM,
        validate_model_on_init=True,
        temperature=0.8,
        num_predict=246
    )

    template = ChatPromptTemplate(
        [
            ("system", system_prompt),
            ("human", "Context: {context}\nQuestion: {question}")
        ]
    )

    chain = template | model 

    result = chain.invoke(
        {"context": context, "question": question}
    )

    return result.content
