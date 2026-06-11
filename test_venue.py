from nodes.venue import venue_node

state = {
    "user_query": "Tell me about Wankhede Stadium"
}

result = venue_node(state)

print(result)