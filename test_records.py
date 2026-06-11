from nodes.records import records_node

state = {
    "user_query": "Highest team score in IPL?"
}

result = records_node(state)

print(result)