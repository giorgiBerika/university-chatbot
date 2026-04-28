- About project:
    This is AI Chat Bot. Created for Ilia State University ( personal project ). It can give you information about academic calendar, argus, payment guide etc. 

- Prerequisites:
    Before you run it, you need to have Ollama installed on you machine + all the packages given into requirements.txt. You can find raw data on the official website of Iliauni. 

- Installation:
    You can clone it: 
        git clone https://github.com/university-chatbot.git
    Create virtual environmetn:
        conda create --name myenv ( suggested py: 3.11.15 )
    Install all the packages:
        pip install -r requirements.txt
    Pull the model:
        ollama pull llama3.2:3b
    
- Run:
    Ingest the data:
        python -m scripts.ingest
    After you got everything run it with:
        streamlit run ui/app.py