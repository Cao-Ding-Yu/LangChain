
from langchain_ollama import ChatOllama

model = ChatOllama(
    model="deepseek-r1:14b",
    # base_url="http://localhost:11434",
)

# 1. 流式调用 Stream
for chunk in model.stream("解释什么是AI"):
    print(chunk.content, end="", flush=True)

# 2. 批量调用 Batch
messages = [
    "中国首都在哪",
    "日本首都在哪",
    "韩国首都在哪",
]

# 按照问题顺序
for response in model.batch(messages):
    print(response.content, end="")

# 按照完成顺序 tuple(index,response)
for response in model.batch_as_completed(messages):
    print(response[1].content, end="")

