from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek

load_dotenv(override=True)

deepseek = ChatDeepSeek(
    model="deepseek-v4-flash",
)

response = deepseek.invoke("用一句话介绍你自己")
print(response)
