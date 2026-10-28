# init_chat_model的在线调用

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv(override=True)

model = init_chat_model( #会根据 model和 provider自动调用 ChatDeepSeek()
    # model="deepseek:deepseek-v4-flash",
    model_provider="deepseek",  #可选
    model="deepseek-v4-flash",
)

response = model.invoke("用一句话介绍你自己")
print(response)

