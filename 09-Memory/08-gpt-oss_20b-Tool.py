# 长期记忆的存取

from typing import NotRequired
from langchain_core.tools import tool
from langgraph.prebuilt import ToolRuntime
from langchain_core.messages import HumanMessage
from langgraph.store.memory import InMemoryStore
from langchain.agents import create_agent, AgentState

store = InMemoryStore()

class CustomState(AgentState):
    user_id : NotRequired[str]

@tool(parse_docstring=True)
def save_user_info(name : str , runtime : ToolRuntime) -> str:
    """
    将客户信息保存在长期记忆中

    Args:
        name : 用户名
        runtime : 工具的运行时

    Returns:
        str : 保存状态
    """
    namespace = ("users",)
    key = runtime.state["user_id"]
    value = {"name" : name}
    runtime.store.put(namespace, key, value)
    return "saved"

@tool(parse_docstring=True)
def get_user_info(runtime : ToolRuntime) -> str:
    """
    从长期记忆中读取客户的信息

    Args:
        runtime : 工具的运行时

    Returns:
        str : 用户信息
    """
    namespace = ("users",)
    key = runtime.state["user_id"]
    item = runtime.store.get(namespace,key)
    return str(item.value) if item else "unknown"

agent = create_agent(
    model="ollama:gpt-oss:20b",
    tools=[save_user_info,get_user_info],
    store=store,
    state_schema=CustomState,
    system_prompt="用户介绍个人信息时，使用工具保存用户信息。用户询问个人信息时，使用工具读取用户信息"
)

response1 = agent.invoke({
    "messages": [HumanMessage("我是小花")],
    "user_id": "user-1"
})

response2 = agent.invoke({
    "messages": [HumanMessage("我叫什么")],
    "user_id": "user-1"
})
for msg in response2["messages"]: msg.pretty_print()

