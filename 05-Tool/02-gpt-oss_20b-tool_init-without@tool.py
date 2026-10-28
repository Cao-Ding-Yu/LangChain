# 使用函数描述创建工具

from rich import print as rprint
from langchain_ollama import ChatOllama
from langchain_core.utils.function_calling import convert_to_openai_tool

model = ChatOllama(
    model="gpt-oss:20b",
    # base_url="http://localhost:11434",
)

# demo1:简洁写法
def get_weather_1(city):
    return f"{city}天气晴朗，气温30度"

# demo2:指定参数类型 parameters.properties
def get_weather_2(city : str):
    return f"{city : str}天气晴朗，气温30度"

# demo3:添加函数描述 description
def get_weather_3(city):
    """查询城市天气"""
    return f"{city}天气晴朗，气温30度"

# demo4:严格按照格式添加注释，写入Args的变量必须指定数据类型
def get_weather_4(city :str):
    """
    查询城市的天气

    Args:
        city : 具体的城市

    Returns:
        返回城市的天气
    """
    return f"{city}天气晴朗，气温30度"

# demo5:变量赋默认值后 parameters.required变化（删减）
def get_weather_5(city = "beijing"):
    """查询城市天气"""
    return f"{city}天气晴朗，气温30度"

# demo6:混合版本
def get_weather(dt:str ,city : str = "beijing"):
    """
    查询城市的天气

    Args:
        city : 具体的城市
        dt : 时间
    """
    return f"{city}天气晴朗，气温30度"

# 函数绑定模型(不带 @tool会默认自动加上)
model_with_tools = model.bind_tools([
    get_weather_1,
    get_weather_2,
    get_weather_3,
    get_weather_4,
    get_weather_5,
    get_weather,
])

rprint(convert_to_openai_tool(get_weather_1))
rprint(convert_to_openai_tool(get_weather_2))
rprint(convert_to_openai_tool(get_weather_3))
rprint(convert_to_openai_tool(get_weather_4))
rprint(convert_to_openai_tool(get_weather_5))
rprint(convert_to_openai_tool(get_weather))