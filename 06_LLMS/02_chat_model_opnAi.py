from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


llm=ChatOpenAI(model="gpt-5.2-pro-2025-12-11",temperature=0.5,max_completion_tokens=19)

print(llm.invoke("where is captal of india").text)