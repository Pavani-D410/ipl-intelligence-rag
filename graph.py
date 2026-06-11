from langgraph.graph import StateGraph, END

from state import IPLState

from nodes.router import router_node
from nodes.routes import route_query

from nodes.batting import batting_node
from nodes.bowling import bowling_node
from nodes.records import records_node
from nodes.venue import venue_node
from nodes.form import form_node
from nodes.h2h import h2h_node

from nodes.synthesis import synthesis_node


graph = StateGraph(IPLState)

# -------------------
# Add Nodes
# -------------------

graph.add_node("router", router_node)

graph.add_node("batting", batting_node)
graph.add_node("bowling", bowling_node)
graph.add_node("records", records_node)
graph.add_node("venue", venue_node)
graph.add_node("form", form_node)
graph.add_node("h2h", h2h_node)

graph.add_node("synthesis", synthesis_node)

# -------------------
# Entry Point
# -------------------

graph.set_entry_point("router")

# -------------------
# Conditional Routing
# -------------------

graph.add_conditional_edges(
    "router",
    route_query,
    {
        "batting": "batting",
        "bowling": "bowling",
        "records": "records",
        "venue": "venue",
        "form": "form",
        "h2h": "h2h"
    }
)

# -------------------
# Connect Nodes to Synthesis
# -------------------

graph.add_edge("batting", "synthesis")
graph.add_edge("bowling", "synthesis")
graph.add_edge("records", "synthesis")
graph.add_edge("venue", "synthesis")
graph.add_edge("form", "synthesis")
graph.add_edge("h2h", "synthesis")

# -------------------
# Final Edge
# -------------------

graph.add_edge("synthesis", END)

# -------------------
# Compile Graph
# -------------------

app = graph.compile()