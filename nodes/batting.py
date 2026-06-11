from nodes.shared_retriever import retriever

def batting_node(state):

    docs = retriever.invoke(
        state["user_query"]
    )

    return {
        "context": docs[0].page_content
    }