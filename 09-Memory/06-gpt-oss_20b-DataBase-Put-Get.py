
from langgraph.store.sqlite import SqliteStore

# 创建时间 != 更新时间：更改时在原有数据库表之上更改

DB_URL = "06-checkpoints.db"

with SqliteStore.from_conn_string(DB_URL) as store:
    store.setup()

    namespace = ("users",)
    user_id = "user-1"
    user_name = "小李"

    store.put(namespace,user_id,{"name":user_name})
    print(store.get(namespace,user_id))
    

