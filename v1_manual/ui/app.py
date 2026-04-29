import streamlit as st 
from pathlib import Path 
import sys 

root =  Path(__file__).parent.parent 
sys.path.insert(0, str(root))

from v1_manual.pipeline.qa import run_query
st.title("Iliauni Chat Bot!")

user_input = st.text_input("Ask Qeustion: ")

if ( st.button("Ask") ):
    ai_response = run_query(user_input)

    col1, col2 = st.columns(2)

    with col1:
        rs = ai_response["response"]
        st.write(f"Bot: {rs}")

    with col2:
        sources = ai_response["source"]
        for s in sources:
            st.write(f"Source: {s}")