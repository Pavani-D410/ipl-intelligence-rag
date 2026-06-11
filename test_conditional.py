from graph import app

result = app.invoke({
    "user_query": "Who has most wickets in IPL?"
})

print(result)