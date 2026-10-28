# 文件夹加载器

from pprint import pprint
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.document_loaders import PythonLoader

directory_loader = DirectoryLoader(
    path="resources",
    glob="*.py", # 文件匹配模式: 匹配python文件
    use_multithreading=True, # 启用多线程
    show_progress=True, # 显示进度条
    loader_cls=PythonLoader # 底层核心加载器
)

docs = directory_loader.load()
print(len(docs))
for doc in docs: pprint(doc)