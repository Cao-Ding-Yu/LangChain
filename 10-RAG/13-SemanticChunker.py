
from langchain_experimental.text_splitter import SemanticChunker
from langchain.embeddings import init_embeddings

# 加载文本字符串
with open("resources/13-ai.txt", encoding="utf-8") as f:
    state_of_the_union = f.read()

# 嵌入模型初始化
embedding_model = init_embeddings(
	model="ollama:qwen3-embedding:8b",
)

text_splitter = SemanticChunker(
    embeddings=embedding_model,
    breakpoint_threshold_type="percentile", # 断点阈值类型：["百分位数", "标准差", "四分位距", "梯度"]
    breakpoint_threshold_amount=20.0,  # 断点阈值数量
    sentence_split_regex=r"(?<=[。？！])\s+"  # 句子切分正则表达式，类似分隔符列表
)
docs = text_splitter.create_documents([state_of_the_union])
for doc in docs: print(f"🔍文档分割: {doc}")

