from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-8b-instant"
)

def synthesis_node(state):

    query = state["user_query"]
    context = state["context"]

    prompt = f"""
You are an IPL RAG assistant.

STRICT RULES:
1. Use ONLY the provided context.
2. Never use outside cricket knowledge.
3. Do not invent facts.
4. If the answer is not present, say:
   "Answer not found in the provided context."
5. Answer in a complete sentence.
6. Include player names, teams, venues and years whenever available.

Context:
{context}

Question:
{query}

Answer:
"""

    response = llm.invoke(prompt)

    return {
        "final_answer": response.content
    }