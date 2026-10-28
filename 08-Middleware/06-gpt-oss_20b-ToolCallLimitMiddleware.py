# 中间件作用：限制工具调用次数

from langchain_core.tools import tool
from langchain.agents import create_agent
from langchain.agents.middleware import ToolCallLimitMiddleware
from langgraph.checkpoint.memory import InMemorySaver
from langchain.messages import HumanMessage

config = {"configurable": {"thread_id": "1"}}

@tool
def add(a:int, b:int):
    """计算两数之和"""
    return a + b

# error → 抛出异常
# end → 程序停止，并返回超额提示
# continue(默认) → 返回错误消息作为ToolMessage，模型切换工具或直接返回结果
agent = create_agent(
    model="ollama:gpt-oss:20b",
    checkpointer=InMemorySaver(),
    tools=[add],
    middleware=[
        ToolCallLimitMiddleware(
            tool_name=None, # 限制指定的工具函数
            thread_limit=10, # 限制每线程总工具调用次数
            run_limit=0, # 限制单次运行总调用次数
            exit_behavior="continue", # 处理行为
        ),
    ],
)

response = agent.invoke({"messages": [HumanMessage("调用工具计算1+1=?")]}, config=config)
for msg in response["messages"]: msg.pretty_print()