from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

llm=ChatAnthropic(model="claude-haiku-5-5")
print(llm.invoke("Who is pm of india").content)

