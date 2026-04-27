from pipeline.qa import run_query

question = input("Enter quesiton: ")
response = run_query( question )
print( response )