# 中间件作用：限制模型调用次数

from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain.agents.middleware import ModelCallLimitMiddleware
from langgraph.checkpoint.memory import InMemorySaver
from langchain.messages import HumanMessage

config = {"configurable": {"thread_id": "1"}}

model = ChatOllama(
    model="gpt-oss:20b",
    # base_url="http://localhost:11434",
)

# 测试 1: 每个线程只能调用两次，超额则退出
agent_end = create_agent(
    model=model,
    checkpointer=InMemorySaver(),
    middleware=[
        ModelCallLimitMiddleware(
            thread_limit=2, # 每个thread最多调用两次模型
            exit_behavior="end", # 默认值，达到限制后退出
        ),
    ],
)

# 测试 2: 单次运行调用模型次数，超额则报错
agent_error = create_agent(
    model=model,
    middleware=[
        ModelCallLimitMiddleware(
            run_limit=0, # 单次运行中最多调用0次模型
            exit_behavior="error", # 达到限制后报错
        ),
    ],
)


# 测试 1: exit_behavior="end"
agent_end.invoke({"messages": [HumanMessage("1+1=?")]}, config=config)
agent_end.invoke({"messages": [HumanMessage("2+2=?")]}, config=config)
response_end = agent_end.invoke({"messages": [HumanMessage("你是谁")]}, config=config)
for msg in response_end["messages"]: msg.pretty_print()

# 测试 2: exit_behavior="error"
response_error = agent_error.invoke({"messages": [HumanMessage("你是谁")]})
for msg in response_error["messages"]: msg.pretty_print()



