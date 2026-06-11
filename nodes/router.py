def router_node(state):

    query = state["user_query"].lower()

    if "run" in query:
        return {"query_type": "batting"}

    elif "wicket" in query:
        return {"query_type": "bowling"}

    elif "score" in query or "record" in query:
        return {"query_type": "records"}

    elif "venue" in query or "stadium" in query:
        return {"query_type": "venue"}

    elif "form" in query:
        return {"query_type": "form"}

    elif "head to head" in query or "vs" in query:
        return {"query_type": "h2h"}

    else:
        return {"query_type": "records"}