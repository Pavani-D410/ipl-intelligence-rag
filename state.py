from typing import TypedDict, List

class IPLState(TypedDict):
    user_query: str
    query_type: str
    context: str
    final_answer: str
    chat_history: List[str]