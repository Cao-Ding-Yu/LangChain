# 工具选型

from langchain_core.tools import tool
from langchain.agents.middleware import LLMToolSelectorMiddleware
from langchain.messages import HumanMessage
from langchain_ollama import ChatOllama
from langchain.agents import create_agent

DEFAULT_SYSTEM_PROMPT = (
    "Your goal is to select the most relevant tools for answering the user's query."
)

@tool
def add(a:int, b:int):
    """计算两数之和"""
    return a + b

model = ChatOllama(
    model="deepseek-r1:14b",
    # base_url="http://localhost:11434",
)

agent = create_agent(
    model="ollama:gpt-oss:20b",
    tools=[add],
    middleware=[
        LLMToolSelectorMiddleware(
            model=model, # 用于控制工具筛选的模型
            max_tools=0, # 除白名单外，最大可调用工具种类总数
            always_include=["add"], # 白名单：排除在限制之外的模型集合
            system_prompt=DEFAULT_SYSTEM_PROMPT, # 工具调用提示词
        ),
    ],
)

response = agent.invoke({"messages": [HumanMessage("调用工具计算1+1=?")]})
for msg in response["messages"]: msg.pretty_print()