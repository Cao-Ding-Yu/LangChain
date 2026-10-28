# 使用@tool定义工具

from typing import Literal
from pydantic import BaseModel, Field
from rich import print as rprint
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_core.utils.function_calling import convert_to_openai_tool

model = ChatOllama(
    model="gpt-oss:20b",
    # base_url="http://localhost:11434",
)

# 方式 1：使用三引号注释
@tool
def get_weather_1(city: str) -> str:
    """获取指定城市的天气信息"""
    return f"{city}晴天，温度 15°C"

# 方式 2：使用description(优先级高于三引号注释)
@tool(description="获取指定城市的天气信息")
def get_weather_2(city: str) -> str:
    """被覆盖的可选描述信息"""
    return f"{city}阴天，温度 25°C"

# 方式 3：使用 parse_docstring：可识别 Args与 Returns
@tool(parse_docstring=True)
def get_weather_3(city: str) -> str:
    """
    获取城市的天气

    Args:
        city : 城市
    """
    return f"{city}阴天，温度 25°C"

# 方式 4：使用 parse_docstring + description：相比单 parse_docstring覆盖了 description
@tool(parse_docstring=True, description="获取指定城市的天气信息")
def get_weather_4(city: str) -> str:
    """
    获取城市的天气

    Args:
        city : 城市
    """
    return f"{city}阴天，温度 25°C"

# 方式 5：使用 name_or_callable参数更改工具名
@tool(description="获取指定城市的天气信息", name_or_callable="getWeather")
def get_weather_5(city: str) -> str:
    return f"{city}阴天，温度 25°C"

# 方式 6：使用 pydantic + args_schema
class WeatherInput(BaseModel):
    city : str # 方式 1：简单创建
    weather : str = Field(
        description="城市天气状况描述",
    ) # 方式 2：加入参数
    unit: Literal["摄氏度", "华氏度"] = Field(
        description="温度单位，必须为'摄氏度'或'华氏度'",
        default="华氏度",
    )# 方式 3：选择栏

@tool(args_schema=WeatherInput)
def get_weather_6(city , weather , unit):
    """获取指定城市的天气信息"""
    return f"{city}城市天气{weather}，温度为15{unit}"

# 方式 7：使用 json_schema
json_schema = {
    'properties': {
        'city': {
            'description': '用户查询天气的城市',
            'type': 'string'
        },
        'unit': {
            'description': '温度单位，必须为摄氏度或华氏度',
            'enum': ['摄氏度', '华氏度'],
            'type': 'string',
        },
        'weather': {
            'default': "暴雨",
            'description': '城市天气状况描述，晴朗或多云或暴雨',
            'type': 'string'
        }
    },
    'required': ['unit', 'city'],
    'type': 'object'
}

@tool(args_schema=json_schema)
def get_weather_7(city, unit, weather):
    """获取指定城市的天气信息"""
    return f"{city}城市天气{weather}，温度为15{unit}"


rprint(convert_to_openai_tool(get_weather_1))
rprint(convert_to_openai_tool(get_weather_2))
rprint(convert_to_openai_tool(get_weather_3))
rprint(convert_to_openai_tool(get_weather_4))
rprint(convert_to_openai_tool(get_weather_5))
rprint(convert_to_openai_tool(get_weather_6))
rprint(convert_to_openai_tool(get_weather_7))

# 绑定工具
model_with_tools = model.bind_tools([
    # get_weather_1,
    # get_weather_2,
    # get_weather_3,
    # get_weather_4,
    # get_weather_5,
    # get_weather_6,
    get_weather_7,
])

# 测试案例
response = model_with_tools.invoke("北京天气如何")
# response = model_with_tools.invoke("2 + 3 = ")
rprint(response.tool_calls)


