from graph import app

result = app.invoke(
    {
        "user_query": "What is Virat Kohli IPL run tally?"
    }
)

print(result)