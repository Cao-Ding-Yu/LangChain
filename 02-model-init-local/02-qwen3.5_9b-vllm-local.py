
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

llm = ChatOpenAI(
    model="/home/cdy/AI/models/Qwen3.5-9B-AWQ-4bit",
    base_url="http://localhost:8000/v1",
    api_key="EMPTY",
    temperature=0.7,
)

messages = [HumanMessage(content="用一句话介绍你自己")]

response = llm.invoke(messages)

print(response.content)

