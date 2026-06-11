def synthesis_node(state):

    context = state["context"]

    answer = f"""
Based on the IPL dataset:

{context}
"""

    return {
        "final_answer": answer
    }