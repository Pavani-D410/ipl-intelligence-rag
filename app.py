from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    "data/IPL_LangGraph_RAG_Dataset.pdf"
)

docs = loader.load()

print(len(docs))