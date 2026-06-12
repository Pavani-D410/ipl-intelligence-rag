from graph import app

chat_history = []

while True:

    query = input("\nAsk IPL Question: ")

    result = app.invoke(
        {
            "user_query": query,
            "chat_history": chat_history
        }
    )

    print("\nAnswer:")
    print(result["final_answer"])

    chat_history.append(
        f"User: {query}"
    )

    chat_history.append(
        f"Assistant: {result['final_answer']}"
    )