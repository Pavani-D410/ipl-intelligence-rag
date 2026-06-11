from graph import app

result = app.invoke(
    {
        "user_query": "Who has most wickets in IPL?"
    }
)

print(result["query_type"])
print(result["final_answer"])