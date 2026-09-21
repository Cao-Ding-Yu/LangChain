
from typing import Union
from langchain_ollama import ChatOllama
from rich import print as rprint
from pydantic import BaseModel, Field
from langchain.agents import create_agent
from langchain.agents.structured_output import ProviderStrategy, ToolStrategy, AutoStrategy

# pydantc | TypedDict | JSON_Schema | @dataclass 均可
class ContractInfo(BaseModel):
    """联系方式"""
    name : str = Field(description="姓名")
    email : str = Field(description="邮箱")
    phone : str = Field(description="电话")

class EventInfo(BaseModel):
    """事件详情"""
    event_name: str = Field(description="事件名称")
    date: str = Field(description="事件发生日期")

model = ChatOllama(
    model="qwen3.8:27b",
    # base_url="http://localhost:11434",
)

messages = {
    "messages": [
        "从以下信息中提取用户信息，小明的邮箱是shkstart@atguigu.com,电话是13012341234",
        # "从这段话中抽取结构化信息：2026年高考报名人数突破1200万",
    ]
}

# 1.  结构化输出方式：ProviderStrategy (没有原生结构化输出能力的模型不支持)
# agent_1 = create_agent(
#     model= model,
#     response_format= ProviderStrategy(schema=ContractInfo),
# )

# rprint(agent_1.invoke(messages))

# 2.  结构化输出方式：ToolStrategy
agent_2 = create_agent(
    model= model,
    response_format= ToolStrategy(schema=ContractInfo),
)

rprint(agent_2.invoke(messages))

# 3.  结构化输出方式：AutoStrategy
agent_3 = create_agent(
    model= model,
    response_format= AutoStrategy(schema=ContractInfo),
)

rprint(agent_3.invoke(messages))

# 混合结构输出(多选一)
agent = create_agent(
    model=model,
    response_format=ToolStrategy(
        schema=Union[ContractInfo, EventInfo],
        tool_message_content="Success", # 设置 Tool content
    )
)

rprint(agent.invoke(messages))



