from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-5.2-pro-2025-12-11")
response = llm.invoke("Who is PM of India")
print(response.content)
