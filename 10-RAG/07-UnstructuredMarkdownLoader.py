
from pprint import pprint
from langchain_community.document_loaders import UnstructuredMarkdownLoader

loader = UnstructuredMarkdownLoader(
    file_path="resources/07-load.md",
    mode= "single", # 加载模式:[single:返回单个Document对象,elements:按标题等元素切分文档]
    strategy="fast", # 解析策略:[fast:快速模式,hi_res:高分辨率模式]
)
print(loader.load())

loader = UnstructuredMarkdownLoader(
    file_path="resources/07-load.md",
    mode= "elements", # 加载模式:[single:返回单个Document对象,elements:按标题等元素切分文档]
    strategy="fast" # 解析策略:[fast:快速模式,hi_res:高分辨率模式]
)

docs = loader.load()
print(len(docs))
for doc in docs: pprint(doc.page_content)

