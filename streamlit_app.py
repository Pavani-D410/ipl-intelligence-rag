import streamlit as st
from graph import app

st.set_page_config(
    page_title="IPL LangGraph RAG Assistant",
    page_icon="🏏",
    layout="wide"
)

st.title(" IPL LangGraph RAG Assistant")

# Store messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input at bottom
query = st.chat_input("Ask anything about IPL...")

if query:

    # User message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    with st.chat_message("user"):
        st.markdown(query)

    # Assistant response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            result = app.invoke(
                {
                    "user_query": query,
                    "chat_history": [
                        f"{m['role']}: {m['content']}"
                        for m in st.session_state.messages
                    ]
                }
            )

            answer = result["final_answer"]

            st.markdown(answer)


    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

# Sidebar
with st.sidebar:

    st.header("Controls")

    if st.button("Clear Chat"):

        st.session_state.messages = []
        st.rerun()