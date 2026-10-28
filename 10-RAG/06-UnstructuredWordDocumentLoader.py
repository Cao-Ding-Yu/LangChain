# docx解析器

from langchain_community.document_loaders import UnstructuredWordDocumentLoader

loader = UnstructuredWordDocumentLoader(
    file_path="resources/06-load.docx",
    mode="single", # 加载模式:[single:返回单个Document对象，elements:按元素切分文档]
)

docs = loader.load()
print(docs)
# 切分对象数量
print(len(docs))

