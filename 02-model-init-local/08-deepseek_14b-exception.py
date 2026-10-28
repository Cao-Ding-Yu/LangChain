# 模型调用的异常捕获

from langchain_ollama import ChatOllama

model = ChatOllama(
    model="deepseek-r1:14b",
    # base_url="http://localhost:11434",
)

try:
    print(model.invoke("一句话介绍你自己"))
except ValueError as e:
    print(e)
except ConnectionError as e:
    print(e)
except Exception as e:
    print(e)

