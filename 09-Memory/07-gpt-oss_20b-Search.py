# 查询长期记忆

from langchain.embeddings import init_embeddings
from langgraph.store.memory import InMemoryStore

# store → namespace → key → value

# 嵌入模型初始化
embedding_model = init_embeddings(
	model="ollama:qwen3-embedding:8b",
)

index_config = {
    "embed": embedding_model,   # 嵌入函数或嵌入模型
    "dims": 1024,               # 嵌入向量的维度
    "fields": ["course"],       # 可选：指定锁定value的某一项
    # "fields": ["$"],          # 可选：默认，索引全部value
}

# 数据初始化
namespace1 = ("users", "Alice", "memories")
key1 = 'preferences'
value1 = {
    "course": "计算机组成原理",
    "sports": "跑步",
    "food": "麻辣香锅"
}

namespace2 = ("users", "Bob", "memories")
key2 = 'preferences'
value2 = {
    "course": "模拟电路",
    "sports": "跑步",
    "food": "板面"
}

namespace3 = ("users", "Black", "memories")
key3 = 'preferences'
value3 = {
    "course": "数字电路",
    "sports": "羽毛球",
    "food": "米线"
}

store = InMemoryStore(index = index_config)
store.put(namespace1, key1, value1)
store.put(namespace2, key2, value2)
store.put(namespace3, key3, value3)

# 1. 查询 1: 查询 namespace
for item in store.search(("users",)): print(item)

# 2. 查询 2: 查询 namespace
for item in store.search(("users","Bob"),): print(item)

# 3. 查询 3: 使用 filter查询 value
for item in store.search(("users",), filter={"food": "米线"}): print(item)

# 4. 查询 4: 使用嵌入函数/模型查询
for item in store.search(("users", ), query="数字电路"): print(item)












