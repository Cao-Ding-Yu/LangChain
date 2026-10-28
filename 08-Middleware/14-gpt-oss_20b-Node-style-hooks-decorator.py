from typing import Any
from langgraph.runtime import Runtime
from langchain.agents import AgentState

from langchain.agents import create_agent
from langchain.agents.middleware import before_model, after_model, before_agent, after_agent
from langchain.messages import HumanMessage

@before_model
def before_model_middleware(state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
    state["messages"][-1].content += "----> before_model <-----"
    return None

@after_model
def after_model_middleware(state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
    state["messages"][-1].content += "----> after_model <-----"
    return None

@before_agent
def before_agent_middleware(state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
    state["messages"][-1].content += "----> before_agent <-----"
    return None

@after_agent
def after_agent_middleware(state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
    state["messages"][-1].content += "----> after_agent <-----"
    return None

agent = create_agent(
    model="ollama:gpt-oss:20b",
    middleware=[
        before_model_middleware,
        after_model_middleware,
        before_agent_middleware,
        after_agent_middleware,
    ],
)

response = agent.invoke({"messages": [HumanMessage("你好")]})
for msg in response["messages"]:msg.pretty_print()