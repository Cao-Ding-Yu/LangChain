# 内存长期记忆的创建时间和更改时间

from langgraph.store.memory import InMemoryStore

# 创建时间 == 更新时间：更改时创建新对象，不在原有之上更改

namespace = ("users",)
user_id = "user-1"
user_name = "小明"

store_memory = InMemoryStore()
store_memory.put(namespace,user_id,{"name":user_name})
print(store_memory.get(namespace,user_id))





