

import streamlit as st
from v2_langchain.pipeline.qa import run_query

st.title("Iliauni Chat Bot!")

user_input = st.text_input("Enter question: ")


if ( st.button("Ask") ):

    answer = run_query(user_input)

    st.write(answer)