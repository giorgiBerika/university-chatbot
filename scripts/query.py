from pipeline.qa import run_query

question = input("Enter quesiton: ")
response = run_query( question )


ai_answer = response.get("response")
sources = response.get("source")


print(f"Response: {ai_answer} \n")
print(f"Sources: {sources}")
