from nodes.batting import batting_node

state = {
    "user_query": "What is Virat Kohli IPL run tally?"
}

result = batting_node(state)

print(result["context"])