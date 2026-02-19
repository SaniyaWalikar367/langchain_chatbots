from langchain_community.chat_message_histories.in_memory import ChatMessageHistory
store={}
store['david']=ChatMessageHistory()
store['david'].add_user_message("what is spoken in france?")
store['david'].add_ai_message("french haha")

store['david'].add_user_message("what is spoken in india?")
print(store)
