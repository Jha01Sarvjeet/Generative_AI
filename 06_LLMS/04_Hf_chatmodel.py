from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint


import os
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="meta-llama/Llama-3.1-8B-Instruct",
                          task="text-generation")



model=ChatHuggingFace(llm=llm)


print(model.invoke("Who is pm of india"))