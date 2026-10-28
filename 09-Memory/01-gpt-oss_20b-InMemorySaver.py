# 内存持久化

from rich import print as rprint
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver

#1、内存持久化器
checkpointer = InMemorySaver()
config = {"configurable":{"thread_id":"1"}}

agent = create_agent(
    model="ollama:gpt-oss:20b",
    checkpointer=checkpointer
)

response1 = agent.invoke({"messages": [HumanMessage("我叫张三")]}, config=config)
print(f"Agent: {response1['messages'][-1].content}")
response2 = agent.invoke({"messages": [HumanMessage("我叫什么")]}, config=config)
print(f"Agent: {response2['messages'][-1].content}")

thread_1_state = agent.get_state(config)
rprint(thread_1_state)
