
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

model = ChatOllama(
    model="deepseek-r1:14b",
    # base_url="http://localhost:11434",
)

# 1. 文本输入
response = model.invoke("用一句话介绍你自己")
print(response)

# 2. 字典列表(多轮对话)
messages = [
    {"role":"system", "content":"你是一个专业的数学家"},
    {"role":"user", "content":"解释一下斐波那契数列"},
]
response = model.invoke(messages)
print(response)

messages.append({"role":"assistant", "content":response.content})
messages.append({"role":"user", "content":"我刚才问了什么问题"})

response = model.invoke(messages)
print(response)

# 3. 消息对象列表(多轮对话)
messages = [
    SystemMessage(content="你是一个专业的数学家"),
    HumanMessage(content="解释一下斐波那契数列"),
]
response = model.invoke(messages)
print(response)

messages.append(AIMessage(content=response.content))
messages.append(HumanMessage(content="我刚才问了什么问题"))

response = model.invoke(messages)
print(response)

