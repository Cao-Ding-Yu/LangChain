
from langchain_core.tools import tool
from langchain.agents.middleware import LLMToolEmulator
from langchain.messages import HumanMessage
from langchain.agents import create_agent

# 用LLM生成的模拟响应来替代真实工具的执行，用于测试

@tool
def add(a:int, b:int):
    """计算两数之和"""
    return a + b

agent = create_agent(
    model="ollama:gpt-oss:20b",
    tools=[add],
    middleware=[
        LLMToolEmulator(
            model="ollama:deepseek-r1:14b", # 用于模拟工具的模型
            tools=[add], # 选择被模拟的工具
        )
    ],
)

response = agent.invoke({"messages": [HumanMessage("调用工具计算1+1")]})
for msg in response["messages"]:msg.pretty_print()