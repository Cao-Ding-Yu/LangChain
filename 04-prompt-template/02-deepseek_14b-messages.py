
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

# 初始化
long_conversation = [
    {"role": "system", "content": "你是 Python 导师"},
    {"role": "user", "content": "什么是列表？用一句解释"}
]
# 第 1 轮
r1 = model.invoke(long_conversation)
long_conversation.append({"role": "assistant", "content": r1.content})
# 第 2 轮
long_conversation.append({"role": "user", "content": "列表和元组有什么区别？用一句话解释"})
r2 = model.invoke(long_conversation)
long_conversation.append({"role": "assistant", "content": r2.content})
# 第 3 轮
long_conversation.append({"role": "user", "content": "什么是字典？用一句解释"})
r3 = model.invoke(long_conversation)
long_conversation.append({"role": "assistant", "content": r3.content})

# 优化后测试(列表和元组有什么区别)
optimized = keep_recent_messages(long_conversation, max_pairs=2)
optimized.append({"role": "user", "content": "我第一个问题问的是什么？"})
response = model.invoke(optimized)
print(f"\nAI 回复: {response.content}")