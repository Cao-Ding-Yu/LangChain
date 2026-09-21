
from typing import Callable
from langchain_core.tools import tool
from langchain_core.messages import ToolMessage
from langgraph.prebuilt.tool_node import ToolCallRequest
from langchain.agents.middleware import AgentMiddleware
from langchain_core.messages import HumanMessage
from langchain.agents import create_agent

@tool(description="计算两数之和")
def add(a: int, b: int) -> int:
    return a+b

class WrapToolCallMiddleware(AgentMiddleware):
    def wrap_tool_call(self, request: ToolCallRequest, handler: Callable[[ToolCallRequest], ToolMessage]) -> ToolMessage:
        result = handler(request)
        print(f"原始参数：{request.tool_call['args']}")
        print(f"原始参数调用结果：{result}")
        request.tool_call["args"]["a"] = 2
        result = handler(request)
        print(f"更新后参数：{request.tool_call['args']}")
        print(f"更新后参数调用结果：{result}")
        return result

agent = create_agent(
    model="ollama:gpt-oss:20b",
    tools=[add],
    middleware=[WrapToolCallMiddleware()],
)

agent.invoke({"messages": [HumanMessage("调用工具计算1+1=?")]})

