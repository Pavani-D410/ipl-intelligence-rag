from nodes.bowling import bowling_node

state = {
    "user_query": "Who has most wickets in IPL?"
}

result = bowling_node(state)

print(result)