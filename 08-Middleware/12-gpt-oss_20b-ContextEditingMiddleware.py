
from langchain_core.tools import tool
from langchain.agents import create_agent
from langchain.agents.middleware import ContextEditingMiddleware, ClearToolUsesEdit
from langchain.messages import HumanMessage, AIMessage
from langgraph.checkpoint.memory import InMemorySaver

# 上下文token压缩

@tool(description="查询指定城市天气")
def get_weather(city: str):
    # 返回一段非常冗长、包含大量 Token 的文本，用于测试中间件的 Token 清理功能
    return (f"当前调用工具，{city}今天天气晴朗，温度20度"
            f"天气非常好，北风，非常适合出行，盼望着，盼望着，"
            f"春天来了。我喜欢春天，你喜欢吗，天气真的很不错"
            f"万里无云，天气晴朗，春和景明，哈哈哈哈哈哈，这是凑字数的"
            f"真不错，天气非常好，适合出行，这里token挺多的"
            f"可以出门玩，可以跑步，钓鱼，爬山，一切都很好哈哈哈")

agent = create_agent(
    model="ollama:gpt-oss:20b",
    tools=[get_weather],
    checkpointer=InMemorySaver(),
    middleware=[
        ContextEditingMiddleware(
            token_count_method="approximate",  # token计算方式: ["approximate", "model"]
            edits=[ # 清理策略列表(可添加自定义策略)
                ClearToolUsesEdit( # 清理策略1: 清理多余工具调用信息
                    trigger=50, # 触发清理的token阈值
                    keep=1, # 保留的最近工具调用结果数
                ),
            ],
        ),
    ],
)

response = None
for i in range(3):
    response = agent.invoke(
        {"messages": [HumanMessage(f"调用工具查看今天北京天气如何，一句话回答")]},
        config={"configurable": {"thread_id": "1"}}
    )

for msg in response["messages"]:
    if isinstance(msg, AIMessage):
        if not msg.tool_calls:
            print(f"本次token用量：{msg.usage_metadata}")
for m in response["messages"]: m.pretty_print()



