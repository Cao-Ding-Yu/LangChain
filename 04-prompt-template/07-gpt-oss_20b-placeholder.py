# 消息占位符的基本使用

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

model = ChatOllama(
    model="gpt-oss:20b",
    # base_url="http://localhost:11434",
)

# 对话历史字典
history = {
    "conversation_1" : [
        ("human","明天的天气如何？"),
        ("ai","明天天气晴朗"),
        ("human","后天的天气怎么样？"),
        ("ai","后天有雨"),
    ],
    "conversation_2": [
        ("human","你很精通机器学习吗"),
        ("ai","是的"),
        ("human","解释什么是梯度下降"),
    ]
}

# 消息占位符的两种使用方法
template = ChatPromptTemplate.from_messages([
    ("system","你是一个Python专家"),
    ("placeholder","{conversation_1}"), # 方式 1：placeholder
    MessagesPlaceholder(variable_name="conversation_2"), # 方式 2：MessagesPlaceholder
])

Input = template.invoke(history)
print(model.invoke(Input).content)

