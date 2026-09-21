
from langchain_core.messages import SystemMessage
from rich import print as rprint
from langchain_ollama import ChatOllama
from langchain.agents import create_agent

# 1. 传入模型实例
model = ChatOllama(
    model="gpt-oss:20b",
    # base_url="http://localhost:11434",
)

agent_1 = create_agent(
    model=model,
    name="agent-1", # 重命名
    system_prompt="你是一名高校的计算机科研助理" # 系统提示词方式 1
)

# 2. 传入模型字符串
agent_2 = create_agent(
    model= "ollama:gpt-oss:20b",
    name="agent-2", # 重命名
    system_prompt=SystemMessage(content="你是一名数学专家"), # 系统提示词方式 2
)

# 对话 1
response_1= agent_1.invoke({
    "messages":[
        {"role":"user","content":"你是什么身份"},
    ]
})
rprint(response_1)

# 对话 2
response_2 = agent_2.invoke({
    "messages" : [
        {"role":"user","content":"你是谁"}
    ]
})
rprint(response_2)