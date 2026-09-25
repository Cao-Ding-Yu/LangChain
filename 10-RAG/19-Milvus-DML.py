
from rich import print as rprint
from langchain.embeddings import init_embeddings
from pymilvus import MilvusClient

client = MilvusClient("http://localhost:19530")

collection_name = "test_collection"

texts = [
    "LangChain 是一个用于构建 LLM 应用的开发框架。",
    "Milvus 是一个适合 AI 应用的向量数据库。",
    "RAG 的核心是先检索相关知识，再让大模型生成答案。",
    "Docker Desktop 可以方便地在本地运行 Milvus Standalone。"
]

# 1. 嵌入模型初始化
embed_model = init_embeddings(
	model="ollama:qwen3-embedding:8b"
)

# 2. 在默认数据库创建数据库表 (静默成功)
client.use_database(db_name='default')
client.create_collection(
    collection_name=collection_name,
    dimension=4096,
    metric_type="COSINE",
)
print(client.list_collections())

# 3. (可选)查看数据库表结构
rprint(client.describe_collection(collection_name=collection_name))

# 4. 生成文本嵌入向量并封装
vectors = embed_model.embed_documents(texts)
data = [
    {
        "id" : i,
        "vector" : vectors[i],
        "text" : texts[i],
    } for i in range(len(texts))
]

# 5. 写入向量数据库
insert_res = client.upsert(
    collection_name=collection_name,
    data=data,
)
# (可选) 强制将内存缓冲区中的数据持久化到磁盘，并立即触发索引构建
client.flush(collection_name=collection_name)

# 6. 检查写入信息
print("stats : ",client.get_collection_stats(collection_name=collection_name))

# 7. 清空collection的全部数据
# client.truncate_collection(collection_name=collection_name)

