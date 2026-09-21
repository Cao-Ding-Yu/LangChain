
from langchain_tavily import TavilySearch
from rich import print as rprint
from langchain.agents import create_agent
from langchain_core.tools import tool

# 1. 调用自定义工具
@tool(parse_docstring=True)
def get_weather(city : str):
    """
    查询城市天气的工具

    Args:
        city : 具体的城市
    """
    return f"{city}天气晴朗，温度是15℃"

agent_1 = create_agent(
    model= "ollama:gpt-oss:20b",
    tools=[get_weather],
)

response = agent_1.invoke({
    "messages" : [
        {"role":"system","content":"你是一个查询天气的助手"},
        {"role":"user","content":"北京天气如何"}
    ]
})
rprint(response)

# 2. 调用内置工具
web_search = TavilySearch(
    max_results=2, # 取查询前两条
    tavily_api_key='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',
)

agent_2 = create_agent(
    model = "ollama:gpt-oss:20b",
    tools = [web_search]
)

response = agent_2.invoke({
    "messages" : [
        {"role": "user", "content": "查询2024年诺贝尔物理学奖得主"}
    ]
})
rprint(response)

# 3. 调用多个工具
agent = create_agent(
    model = "ollama:gpt-oss:20b",
    tools = [web_search,get_weather],
)

response = agent.invoke({
    "messages" : [
        {"role": "user", "content": "今天北京天气如何，说一条新闻"}
    ]
})
rprint(response)

