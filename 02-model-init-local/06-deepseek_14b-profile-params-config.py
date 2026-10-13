from rich import print as rprint
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_deepseek import ChatDeepSeek
from langchain_core.runnables import ConfigurableField

model = ChatOllama(
    model="deepseek-r1:14b",
    # base_url="http://localhost:11434",

    # extra_body参数列表：模型厂商基于OpenAI新增的字段
    # extra_body={"thinking": {"type": "disabled"}},

    # model_kwargs参数列表：模型本身支持，但LangChain中没有的参数
    # model_kwargs={"tools": [
    #     {
    #         "type": "function",
    #         "function": {
    #             "name": "get_weather",
    #             "description": "Get weather of a location, the user should supply a location first.",
    #             "parameters": {
    #                 "type": "object",
    #                 "properties": {
    #                     "location": {
    #                         "type": "string",
    #                         "description": "The city and state, e.g. San Francisco, CA",
    #                     }
    #                 },
    #                 "required": ["location"]
    #             },
    #         }
    #     },
    # ]}
)

deepseek = ChatOpenAI(
    model="deepseek-r1:14b",
    api_key="OpenAI_API_KEY",
    base_url="OpenAI_API_BASE",
    configurable_fields=("model", "model_provider"),
)

# 1. 查看模型属性(支持输入输出内容格式，最大输入输出token数，支持使用工具等)
print(model.profile)

# 2. 查看模型初始化支持参数
print(ChatDeepSeek.model_fields.keys())
print(ChatOpenAI.model_fields.keys())
print(ChatOllama.model_fields.keys())

# 3. 新建实例调用config参数(本地+云端)
config = {
    "configurable":{
        "model": "qwen3.8:27b",
    }
}

configurable_model = model.configurable_fields(model=ConfigurableField(id="model"),)
rprint(configurable_model.invoke("用一句话介绍你自己",config=config))

# 4. 动态更改config参数(云端)
rprint(deepseek.invoke("用一句话介绍你自己",config=config))


