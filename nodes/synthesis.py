from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-8b-instant"
)

def synthesis_node(state):

    query = state["user_query"]
    context = state["context"]

    history = "\n".join(
        state.get("chat_history", [])
    )

    prompt = f"""
You are an IPL assistant.

Previous Conversation:
{history}

Retrieved Context:
{context}

Current Question:
{query}

Rules:
- Use context first.
- Use previous conversation when resolving references like "he", "they", "that player".
- Give concise answers.

Answer:
"""

    response = llm.invoke(prompt)

    return {
        "final_answer": response.content
    }