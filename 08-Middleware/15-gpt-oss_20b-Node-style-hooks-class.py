
from typing import Any
from langgraph.runtime import Runtime
from langchain.agents import AgentState

from langchain.agents import create_agent
from langchain.agents.middleware import AgentMiddleware
from langchain.messages import HumanMessage

class MyMiddleware(AgentMiddleware):
    def before_model(self,state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
        state["messages"][-1].content += "----> before_model <-----"
        return None

    def after_model(self,state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
        state["messages"][-1].content += "----> after_model <-----"
        return None

    def before_agent(self,state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
        state["messages"][-1].content += "----> before_agent <-----"
        return None

    def after_agent(self,state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
        state["messages"][-1].content += "----> after_agent <-----"
        return None

agent = create_agent(
    model="ollama:gpt-oss:20b",
    middleware=[
        MyMiddleware(),
    ],
)

response = agent.invoke({"messages": [HumanMessage("你好")]})
for msg in response["messages"]:msg.pretty_print()