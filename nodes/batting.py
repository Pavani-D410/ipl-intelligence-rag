from nodes.shared_retriever import retriever

def batting_node(state):

    docs = retriever.invoke(
        state["user_query"]
    )

    context = "\n\n".join(
    [doc.page_content for doc in docs[:3]]
)

    return {
    "context": context
}