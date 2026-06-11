def router_node(state):

    query = state["user_query"].lower()

    if "run" in query:
        return {
            "query_type": "batting"
        }

    elif "wicket" in query:
        return {
            "query_type": "bowling"
        }

    elif "record" in query:
        return {
            "query_type": "records"
        }

    return {
        "query_type": "general"
    }