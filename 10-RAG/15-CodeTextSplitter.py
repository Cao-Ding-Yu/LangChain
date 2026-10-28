# 代码切分器

from pprint import pprint
from langchain_text_splitters import Language, RecursiveCharacterTextSplitter

# 支持分割的编程语言
print([e.value for e in Language])

# python代码段
PYTHON_CODE = """
def hello_world():
    print("Hello, World!")

def hello_world1():
    print("Hello, World1!")
"""

python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=50,
    chunk_overlap=0,
)

python_docs = python_splitter.create_documents([PYTHON_CODE])
pprint(python_docs)