# Milvus的DQL操作

from langchain.embeddings import init_embeddings
from pymilvus import MilvusClient

# 数据库初始化
client = MilvusClient("http://localhost:19530")
client.use_database(db_name='default')

collection_name = "test_collection"

# 1. 全量输出
iterator = client.query_iterator(
    collection_name=collection_name,
    filter="",
    output_fields=["*"]
)
while True:
    rows = iterator.next()
    if not rows: break
    for row in rows:
        print(f"id : {row["id"]},vector = {row["vector"][:5]},text = {row["text"]}")
iterator.close()
print('-'*50)

# 2. 主键查询
res = client.get(
    collection_name=collection_name,
    ids=[0,1,2]
)
for i in range(len(res)):
    print(f"id : {res[i]["id"]},vector = {res[i]["vector"][:5]},text = {res[i]["text"]}")
print('-'*50)

# 3. 相似度检索
query_1 = "什么是向量数据库"
query_2 = "什么是LangChain"
model = init_embeddings(model="ollama:qwen3-embedding:8b")
query_vector_1 = model.embed_query(query_1)
query_vector_2 = model.embed_query(query_2)

results = client.search(
    collection_name=collection_name,
    data=[query_vector_1,query_vector_2], # 查询内容列表
    limit=3, # 取最相关的三条
    output_fields=["text"] # 只显示text文本
)
for res in results: print(res)


