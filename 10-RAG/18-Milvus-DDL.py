
from pymilvus import MilvusClient

# 1. 连接数据库
client = MilvusClient("http://localhost:19530")

# 2. 创建数据库 (重复会报错)
db_name = "rag_test"
if db_name not in client.list_databases():
    client.create_database(db_name=db_name)

# 3. 查看当前数据库列表
for db in client.list_databases():
    print(db)

# 4. 删除数据库 (可重复不报错,但需要先删除全部collections)
client.drop_database(db_name = db_name)

# 5. 切换数据库
client.use_database(db_name='default')

# 6. 创建数据库下collection
collection_name = "test_collection"
client.create_collection(
    collection_name=collection_name, # 命名
    dimension=4096, # 向量维度
    metric_type="COSINE", # 相关度计算函数 (余弦相似度)
)

# 7. 查看数据库下collections
for coll in client.list_collections():
    print(coll)

# 8. 删除collection
client.drop_collection(collection_name=collection_name)



