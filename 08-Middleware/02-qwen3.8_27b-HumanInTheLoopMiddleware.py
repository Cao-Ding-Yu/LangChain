
from rich import print as rprint
from langchain.tools import tool
from langgraph.types import Command
from langchain.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware

# 中间件作用：人为限制工具执行权限

@tool
def get_weather(city: str, is_forcast: bool = False) -> str:
    """
    查询指定城市天气

    Args:
        city: 城市名称
        is_forcast: 是否包含明日天气预报？
    """
    res = f"{city}今天天气晴朗"
    if is_forcast: res += "明天有雨"
    return res

@tool
def get_news() -> str:
    """
    查询当日新闻
    """
    return "中方三艘油轮通过霍尔木兹海峡"

@tool
def read_email_tool(email_id: str) -> str:
    """通过邮件ID读取内容"""
    return f"邮件ID：{email_id}\n是空的"

@tool
def send_email_tool(recipient: str, subject: str, body: str) -> str:
    """发送邮件"""
    print(">>> 发送邮件")
    return f"发送给 {recipient} 的邮件标题是：{subject}，内容：{body}"

# 1. 定义智能体
agent = create_agent(
    model= "ollama:qwen3.8:27b",
    tools=[read_email_tool, send_email_tool, get_weather, get_news],
    checkpointer=InMemorySaver(),
    middleware=[
        HumanInTheLoopMiddleware(
            interrupt_on={ # 为每个工具定义是否人工确认
                "get_weather": True, # True表示默认拦截
                "get_news": True, # 选项 ['approve', 'edit', 'reject']
                "read_email_tool": False, # False表示默认不拦截
                "send_email_tool": { # 自定义设置
                    "allowed_decisions": ["approve", "reject"], # 自定义拦截选项
                    "description": "发送邮件中断" # 自定义拦截描述
                },
            },
            description_prefix="中断了", # 默认拦截描述
        ),
    ]
)

# 2. 创建对话
response = agent.invoke(
    input={
        "messages": [
            HumanMessage(content="请帮我查询今天北京的天气，查询今日新闻，查看ID为'sk2131421'的邮件内容，向843941787@qq.com发送邮件，标题是'哈哈哈'，内容是：'你好啊'，同时做这四件事")
        ]
    },
    config={"configurable": {"thread_id": "1"}}
)
rprint(response)

# 3. 设置工具 decision
weather_decision = {
    "type" : "edit",
    "edited_action" : {
        "name" : "get_weather",
        "args" : {"city" : "上海市","is_forcast" : True},
    }
}

news_decision = {
    "type" : "approve"
}

send_email_decision = {
    "type" : "approve"
}


decisions = {
    "decisions" : list()
}

# 4. 传入 decision并继续执行
action_requests = response.get("__interrupt__")[0].value["action_requests"]
if action_requests:
    for action_request in action_requests:
        if action_request["name"] == "get_weather":
            decisions["decisions"].append(weather_decision)
        if action_request["name"] == "get_news":
            decisions["decisions"].append(news_decision)
        if action_request["name"] == "send_email_tool":
            decisions["decisions"].append(send_email_decision)
    # 5. 模型继续运行与结果打印
    response = agent.invoke(
        Command(resume=decisions),
        config={"configurable": {"thread_id": "1"}}
    )
    for msg in response["messages"]: msg.pretty_print()




