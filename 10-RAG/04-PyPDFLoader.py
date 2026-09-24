
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    file_path="resources/04-05-11-load.pdf",  # 本地文件
    # file_path="https://arxiv.org/pdf/alg-geom/9202012", # 在线链接
    extraction_mode="plain", # plain:默认值，普通文本提取; layout:布局感知提取模式
)

docs = loader.load()
print(docs)
print(len(docs)) # 文档页数

