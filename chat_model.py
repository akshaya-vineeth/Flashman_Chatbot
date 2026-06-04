from dotenv import load_dotenv
load_dotenv()

import os
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage , SystemMessage , HumanMessage

model = ChatMistralAI(model = "mistral-small-2506")

message_history = [
    SystemMessage(content="You are a normal Ai agent")

]

print("Welcome to Flashman 1.0 \n Press 0 to exit")

while True:

    prompt = input("User:")
    message_history.append(HumanMessage(content=prompt))
    if prompt == "0":
        break
    response = model.invoke(message_history)
    message_history.append(AIMessage(content=response.content))

    print("Agent :",response.content)

