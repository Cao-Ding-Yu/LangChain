# 工具的手动调用

from rich import print as rprint
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain.messages import HumanMessage
from pydantic import BaseModel, Field
from langchain_core.utils.function_calling import convert_to_openai_tool

model = ChatOllama(
    model="gpt-oss:20b",
    # base_url="http://localhost:11434",
)

# 工具 ：获取当日及次日天气
class WeatherSchema(BaseModel):
    city: str = Field(default="北京", description="城市名称")
    forecast: bool = Field(default=False, description="是否包含明日天气")

@tool(
    name_or_callable="Get_Weather",
    description="获取当日或次日城市天气的工具",
    args_schema=WeatherSchema,
    parse_docstring=True
)
def get_weather(city, forecast) -> str:
    """
    查询当日的天气，可以包含明天的天气预报

    Args:
        city : 城市的名称
        forecast : 是否包含明日的天气
    """
    result = f"{city}天气晴朗，气温15度"
    if forecast: result += "明天有雨，气温5度"
    return result

rprint(convert_to_openai_tool(get_weather)) # 代码比注释文档优先级高

# 1. 模型绑定工具
model_with_tools = model.bind_tools([get_weather])

# 2. 消息列表初始化
messages = [HumanMessage("今天杭州天气如何,明天天气如何")]

# 3. 更新 AIMessage
response = model_with_tools.invoke(messages)
messages.append(response)

# 4. 更新 ToolMesssage
for tool_call in response.tool_calls:
    # 大模型和Agent的区别在于：大模型不会主动的调用工具，需要主动让工具调用。
    if tool_call["name"] == "Get_Weather":
        tool_response = get_weather.invoke(tool_call)
        messages.append(tool_response)

# 5. 生成最终AIMessage，打印全部 Messages == user -> ai -> tool -> ai -> (user)
messages.append(model_with_tools.invoke(messages))
for msg in messages: msg.pretty_print()

