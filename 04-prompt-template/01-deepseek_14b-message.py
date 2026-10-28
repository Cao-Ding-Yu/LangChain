# 消息的创建方法

from rich import print as rprint
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage

model = ChatOllama(
    model="deepseek-r1:14b",
    # base_url="http://localhost:11434",
)

# 消息格式_1
messages_1 = [
    {"role":"system","content":"你是一个友好的AI助手"},
    {"role":"user","content":"1 + 2 = ?"},
    {"role":"assistant","content":"3"},
    {"role":"user","content":"我刚才问了什么问题？"},
]

# 消息格式_2
messages_2 = [
    SystemMessage(content="你是一个友好的AI助手"),
    HumanMessage("1 + 2 = ?"),
    AIMessage("3"),
    HumanMessage("我刚才问了什么问题？"),
]

# name参数的使用
messages_3 = [
    SystemMessage("你是一个信息抽取器。你会收到多条来自不同发言者的 user 消息。每条消息可能带有 name 字段。你的任务是：严格根据每条消息的 name 提取发言者及其观点，并输出 JSON。禁止使用“第一个人/第二个人”这种相对称呼。若某条消息没有 name，则输出 unknown。输出格式：{\"speakers\":[{\"name\":\"...\",\"claim\":\"...\"}]}"),
    HumanMessage(content="我认为 1+1=2", name="Bob"),
    HumanMessage(content="我认为 1+1>2", name="Tom"),
    HumanMessage(content="请列出谁说了什么，不判断对错", name="audience"),
]

# ToolMessage类的使用
ai_message = AIMessage(
    content=[],
    tool_calls=[{
        "name": "get_weather",
        "args": {"location": "北京"},
        "id": "call_00_nUD2NC9QRN5Cg1GaoIkBJQ4s"
    }]
)

tool_message = ToolMessage(
    content="今天北京天气晴朗，万里无云~",
    tool_call_id = "call_00_nUD2NC9QRN5Cg1GaoIkBJQ4s"
)

messages = [
    HumanMessage(content="北京天气如何"),
    ai_message,
    tool_message,
]

response = model.invoke(messages)
rprint(response)