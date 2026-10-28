# 删除上下文

from typing import Any
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain.messages import RemoveMessage
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent, AgentState
from langchain.agents.middleware import after_model
from langgraph.runtime import Runtime
from langchain_core.messages import HumanMessage

config = {"configurable": {"thread_id": "1"}}

@after_model
def delete_old_messages(state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
    messages = state["messages"]
    if len(messages) > 4:
        return {"messages": [RemoveMessage(id=m.id) for m in messages[:len(messages)-4]]}
    return None

DB_PATH = "03-checkpoints.db"

with SqliteSaver.from_conn_string(DB_PATH) as checkpointer:
    checkpointer.setup()
    agent = create_agent(
        model="ollama:gpt-oss:20b",
        checkpointer=InMemorySaver(),
        middleware=[delete_old_messages],
    )

    agent.invoke({"messages": [HumanMessage("1+1=?")]}, config)
    agent.invoke({"messages": [HumanMessage("2+2=?")]}, config)
    agent.invoke({"messages": [HumanMessage("3+3=?")]}, config)
    response = agent.invoke({"messages": [HumanMessage("4+4=?")]}, config)
    for msg in response["messages"]: msg.pretty_print()



