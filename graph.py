from langgraph.graph import StateGraph, END

from state import IPLState
from nodes.router import router_node
from nodes.batting import batting_node

graph = StateGraph(IPLState)

# Nodes
graph.add_node("router", router_node)
graph.add_node("batting", batting_node)

# Entry Point
graph.set_entry_point("router")

# Flow
graph.add_edge("router", "batting")
graph.add_edge("batting", END)

app = graph.compile()