# 调用Ollama模型

from langchain_ollama import ChatOllama
from langchain.chat_models import init_chat_model

# 方式 1
model = ChatOllama(
    model="deepseek-r1:14b",
    # base_url="http://localhost:11434",
)

# 方式 2
# model = init_chat_model(
#     model="deepseek-r1:14b",
#     model_provider="ollama",
#     # base_url="http://localhost:11434",
# )

response = model.invoke("用一句话介绍你自己")
print(response)

