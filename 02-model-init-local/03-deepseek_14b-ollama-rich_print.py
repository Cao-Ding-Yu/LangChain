
from rich import print as rprint
from langchain_ollama import ChatOllama

model = ChatOllama(
    model="deepseek-r1:14b",
    # base_url="http://localhost:11434",
)

response = model.invoke("用一句话介绍你自己")

# 0. 结构化输出
rprint(response)

# 1. 内容
print(response.content)

# 2. ID
print(response.id)

# 3. Token
print(response.usage_metadata)

# 4. 元数据
meta = response.response_metadata
print(meta['model'])
print(meta['done_reason'])
print(meta['model_provider'])

