
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

text="LangChain框架特性\n\n多模型集成(GPT/Claude)\n记忆管理功能\n链式调用设计。文档分析场景示例：需要处理PDF/Word等格式。"

# 1. 按照默认分隔符列表顺序递归分割字符串 (split_text ← 字符串)
splitter_1 = RecursiveCharacterTextSplitter(
    chunk_size=10,  # 分割块大小
    chunk_overlap=0,  # 块间重叠字符数
    # separators=["\n\n", "\n", " ", ""], # 默认，分隔符列表
)
paragraphs = splitter_1.split_text(text)
for chunk in paragraphs:
    print(len(chunk))
    print(chunk)
print('-' * 50)

# 2. 按照默认分隔符列表顺序递归分割字符串列表，并添加索引 (create_documents ← 字符串列表)
splitter_2 = RecursiveCharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=0,
    add_start_index=True, # 分割块在原文起始索引
)
paragraphs = splitter_2.create_documents([text])
for para in paragraphs: print(para)
print('-' * 50)

# 3. 加载PDF文件后分割 (split_documents ← Document对象列表)
loader = PyPDFLoader("resources/04-05-11-load.pdf")
docs = loader.load()   # 返回Document对象

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=120,
    chunk_overlap=5,
    add_start_index=True,
)
paragraphs = text_splitter.split_documents(docs)
for para in paragraphs: print(para)



