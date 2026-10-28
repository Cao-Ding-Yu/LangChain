# LangSmith的基本使用

from dotenv import load_dotenv
from rich import print as rprint
from langchain_ollama import ChatOllama
from langchain_core.runnables import ConfigurableField

load_dotenv(override=True)

model = ChatOllama(
    model="deepseek-r1:14b",
    # base_url="http://localhost:11434",
)

# 1. 直接查看
response = model.invoke("用一句话介绍你自己")
print(response)

# 2. 更改参数
config = {
    "run_name": "LangChain",
    "configurable":{
        "model": "qwen3.8:27b",
    }
}

configurable_model = model.configurable_fields(model=ConfigurableField(id="model"),)
rprint(configurable_model.invoke("用一句话介绍你自己",config=config))



