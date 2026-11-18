from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(model="gpt-5.4-mini")

messages=[
    SystemMessage(content="you are a Helpful assistent"),
    HumanMessage(content='Tell me about LanGchain')
    
    
    
]

result=model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)

