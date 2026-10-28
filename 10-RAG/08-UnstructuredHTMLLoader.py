# HTML解析器

from pprint import pprint
from langchain_community.document_loaders import UnstructuredHTMLLoader

# strategy:
#   "fast"：解析文件速度较快,但可能丢失部分结构或元数据
#   "hi_res"：解析精准，但速度慢一些
#   "ocr_only"：强制使用ocr，仅仅适用于图像

loader = UnstructuredHTMLLoader(
    file_path="resources/08-load.html",
    mode="elements",
    strategy="fast"
)

docs = loader.load()
print(len(docs))
for doc in docs: pprint(doc.page_content)