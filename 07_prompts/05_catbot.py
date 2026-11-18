from langchain_core import chat_history
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage

from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI(model="gpt-5.4-mini")
message=[SystemMessage(content="You are a elpful assistent ")]

while True:
    user_input=input("You: ")
    message.append(HumanMessage(content=user_input))
    if user_input.lower()=="exit":
        break
    result=model.invoke(message)
    message.append(AIMessage(content=result.content))
    
    print("response:  " ,result.text)
print(message)

