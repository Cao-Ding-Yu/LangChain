
from langchain_ollama import ChatOllama

model = ChatOllama(
    model="deepseek-r1:14b",
    # base_url="http://localhost:11434",
)

# 保留最近几轮对话
def keep_recent_messages(messages, max_pairs = 3):
    system_messages = [m for m in messages if m.get("role") == "system"]
    conversation_messages = [m for m in messages if m.get("role") != "system"]
    recent_messages = conversation_messages[-2*max_pairs:]
    return system_messages + recent_messages

messages = [
    {"role": "system","content":"你是小谷姐姐，是尚硅谷教育的数字员工，也是一名耐心、友好的AI助手，可以回答学的问题"},
]

while True:
    # 用户输入
    user_input = input("\n请输入：")
    messages.append({"role": "user","content": user_input})

    # AI回复
    print("小萝莉姐姐：",end="",flush=True)
    reply_content = str() # 回复内容
    memory_messages = keep_recent_messages(messages, max_pairs=5)
    for chunk in model.stream(memory_messages):
        print(chunk.content,end="",flush=True)
        reply_content += chunk.content
    messages.append({"role":"assistant", "content": reply_content})

