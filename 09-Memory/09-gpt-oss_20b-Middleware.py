
from typing import Any
from langchain.agents import create_agent
from langchain.agents.middleware import AgentMiddleware, AgentState
from langchain_core.messages import HumanMessage
from langgraph.store.sqlite import SqliteStore
from langgraph.runtime import Runtime

FRUITS = {"苹果", "香蕉", "橙子", "葡萄", "西瓜", "草莓", "芒果",}

class FruitMemoryMiddleware(AgentMiddleware):
    def after_model(self, state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
        messages = state.get("messages", [])
        found_fruits = set()
        for msg in messages:
            if isinstance(msg, HumanMessage) and isinstance(msg.content, str):
                found_fruits.update(fruit for fruit in FRUITS if fruit in msg.content)
        if found_fruits:
            for fruit in found_fruits:
                runtime.store.put(("fruits",), fruit, {"name": fruit, "weight": 1})
        return None


DB_PATH = "09-checkpoints.db"

with SqliteStore.from_conn_string(DB_PATH) as store:
    store.setup()
    agent = create_agent(
        model="ollama:gpt-oss:20b",
        middleware=[FruitMemoryMiddleware()],
        store=store,
    )
    agent.invoke({"messages": [HumanMessage("我喜欢吃苹果和香蕉")]})
    agent.invoke({"messages": [HumanMessage("我还喜欢西瓜")]})
    agent.invoke({"messages": [HumanMessage("橙子和草莓也不错")]})
    items = store.search(("fruits",))
    for item in items: print(item)

