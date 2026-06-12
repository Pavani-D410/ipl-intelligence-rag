from graph import app

while True:

    query = input("\nAsk IPL Question: ")

    if query.lower() == "exit":
        break

    result = app.invoke(
        {
            "user_query": query
        }
    )

    print("\nAnswer:")
    print(result["final_answer"])