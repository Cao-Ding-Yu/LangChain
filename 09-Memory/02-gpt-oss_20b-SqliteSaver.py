
from langchain.agents import create_agent
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain_core.messages import HumanMessage

DB_PATH = "02-checkpoints.db"

with SqliteSaver.from_conn_string(DB_PATH) as checkpointer:
    checkpointer.setup()
    agent = create_agent(
        model="ollama:gpt-oss:20b",
        checkpointer=checkpointer
    )
    config = {"configurable": {"thread_id": "1"}}
    response1 = agent.invoke({"messages": [HumanMessage("我是小王")]}, config=config)
    response2 = agent.invoke({"messages": [HumanMessage("我叫什么")]}, config=config)
    for msg in response2['messages']: msg.pretty_print()

