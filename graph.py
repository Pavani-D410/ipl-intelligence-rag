from langgraph.graph import StateGraph, END

from state import IPLState
from nodes.router import router_node
from nodes.batting import batting_node
from nodes.bowling import bowling_node
from nodes.records import records_node
from nodes.routes import route_query

graph = StateGraph(IPLState)

graph.add_node("router", router_node)
graph.add_node("batting", batting_node)
graph.add_node("bowling", bowling_node)
graph.add_node("records", records_node)

graph.set_entry_point("router")

graph.add_conditional_edges(
    "router",
    route_query,
    {
        "batting": "batting",
        "bowling": "bowling",
        "records": "records"
    }
)

graph.add_edge("batting", END)
graph.add_edge("bowling", END)
graph.add_edge("records", END)

app = graph.compile()