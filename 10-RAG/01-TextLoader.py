# 文本加载器

from langchain_community.document_loaders import TextLoader

loader = TextLoader(
    file_path="resources/01-load-utf-8.txt",
    encoding="utf-8",
)
print(loader.load())

loader = TextLoader(
    file_path="resources/01-load-gbk.txt",
    encoding="gbk",
)
print(loader.load())

