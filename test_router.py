from nodes.router import router_node

state = {
    "user_query": "What is Virat Kohli run tally?"
}

result = router_node(state)

print(result)