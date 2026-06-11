from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = FAISS.load_local(
    "faiss_db",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever()

def batting_node(state):

    docs = retriever.invoke(
        state["user_query"]
    )

    return {
        "context": docs[0].page_content
    }