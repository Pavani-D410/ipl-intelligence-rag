from nodes.synthesis import synthesis_node

state = {
    "context": "Virat Kohli has scored 7263 IPL runs."
}

result = synthesis_node(state)

print(result["final_answer"])