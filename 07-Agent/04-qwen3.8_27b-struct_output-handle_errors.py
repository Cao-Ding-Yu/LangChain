# 结构化输出异常捕获方法

from typing import Union
from langchain.agents.structured_output import ToolStrategy, MultipleStructuredOutputsError, StructuredOutputValidationError
from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field
from rich import print as rprint
from langchain.agents import create_agent

class ContactInfo(BaseModel):
    """联系方式"""
    name: str = Field(description="姓名")
    email: str = Field(description="电子邮箱")

class EventDetails(BaseModel):
    """活动详情"""
    event_name: str = Field(description="活动名称")
    date: str = Field(description="活动日期")

model = ChatOllama(
    model="qwen3.8:27b",
    # base_url="http://localhost:11434",
)

messages = {
    "messages": [
        "提取以下文本中内容：姓名：张三，电子邮箱：zhang3@atguigu.com，活动名称：公司年会，活动日期：2026-07-15",
    ]
}


# 1. handle_errors = True：默认，捕获异常
agent_1 = create_agent(
    model= model,
    response_format=ToolStrategy(
        schema=Union[ContactInfo, EventDetails],
        handle_errors=True
    )
)
rprint(agent_1.invoke(messages))

# 2. handle_errors = False：不捕获异常，直接报错
# agent_2 = create_agent(
#     model= model,
#     response_format=ToolStrategy(
#         schema=Union[ContactInfo, EventDetails],
#         handle_errors=False
#     )
# )
# rprint(agent_2.invoke(messages))

# 3. handle_errors = str：捕获异常并显示字符串内容作为错误信息
agent_3 = create_agent(
    model= model,
    response_format=ToolStrategy(
        schema=Union[ContactInfo, EventDetails],
        handle_errors="出错啦"
    )
)
rprint(agent_3.invoke(messages))

# 4. handle_errors = 异常类型：捕获指定异常，其余异常报错
agent_4 = create_agent(
    model= model,
    response_format=ToolStrategy(
        schema=Union[ContactInfo, EventDetails],
        handle_errors=(MultipleStructuredOutputsError,StructuredOutputValidationError),
    )
)
rprint(agent_4.invoke(messages))

# 5. handle_errors = 自定义错误处理函数：捕获异常，执行指定函数
def custom_error_handler(error : Exception) -> str:
    """自定义错误处理函数"""
    error_str = str(error)
    print(f"捕获到的错误类型是：{type(error).__name__}")
    print(f"错误详情:{error_str}")
    if isinstance(error, MultipleStructuredOutputsError):
        return "检测到多个响应，请选择最相关的一个进行返回"
    elif isinstance(error, StructuredOutputValidationError):
        return "数据格式有误，请检查字段是否符号要求。"
    else : return f"Error:{error_str}"

agent_5 = create_agent(
    model= model,
    response_format=ToolStrategy(
        schema=Union[ContactInfo, EventDetails],
        handle_errors=custom_error_handler,
    )
)
rprint(agent_5.invoke(messages))

