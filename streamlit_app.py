import streamlit as st
from graph import app

st.title("IPL LangGraph RAG Assistant")

query = st.text_input("Ask an IPL Question")

if st.button("Submit"):

    result = app.invoke(
        {"user_query": query}
    )

    st.write(result["final_answer"])