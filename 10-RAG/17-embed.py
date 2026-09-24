
from langchain_community.document_loaders import CSVLoader
from langchain.embeddings import init_embeddings

text = "你好，很高兴认识你"

embedding_model = init_embeddings(
    model="ollama:qwen3-embedding:8b"
)

# 句子向量化
embed_docs = embedding_model.embed_query(text)
print(len(embed_docs))
print(embed_docs)
print('-'*50)

# 文档向量化
loader = CSVLoader("resources/02-17-load.csv", encoding="utf-8")
docs = loader.load_and_split()
texts = [doc.page_content for doc in docs]
embeded_docs = embedding_model.embed_documents(texts)
for i in range(len(texts)):
    print(f"{texts[i]}\n{embeded_docs[i][:3]}",end="\n\n")


