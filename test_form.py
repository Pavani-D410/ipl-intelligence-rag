from nodes.form import form_node

state = {
    "user_query": "How is CSK recent form?"
}

result = form_node(state)

print(result)