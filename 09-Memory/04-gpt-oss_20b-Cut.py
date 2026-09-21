
from typing import Any
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain.messages import RemoveMessage
from langgraph.graph.message import REMOVE_ALL_MESSAGES
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent, AgentState
from langchain.agents.middleware import before_model
from langgraph.runtime import Runtime
from langchain_core.messages import HumanMessage

config = {"configurable": {"thread_id": "1"}}

@before_model
def cut_messages(state:AgentState,runtime:Runtime) -> dict[str, Any] | None:
    messages = state["messages"]
    if len(messages) < 3: return None
    new_messages = [messages[0]] + messages[-1:]
    return {
        "messages": [
            RemoveMessage(id=REMOVE_ALL_MESSAGES), # 特殊指令：删除全部上下文
            *new_messages # 解包新的上下文列表
        ],
    }

DB_PATH = "04-checkpoints.db"

with SqliteSaver.from_conn_string(DB_PATH) as checkpointer:
    agent = create_agent(
        model="ollama:gpt-oss:20b",
        checkpointer=InMemorySaver(),
        middleware=[cut_messages],
    )

    agent.invoke({"messages": [HumanMessage("1+1=?")]}, config)
    agent.invoke({"messages": [HumanMessage("2+2=?")]}, config)
    agent.invoke({"messages": [HumanMessage("3+3=?")]}, config)
    response = agent.invoke({"messages": [HumanMessage("4+4=?")]}, config)
    for msg in response["messages"]: msg.pretty_print()



