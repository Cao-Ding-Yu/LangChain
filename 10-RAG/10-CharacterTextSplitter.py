# 字符文本切分器

from langchain_text_splitters import CharacterTextSplitter

text = "LangChain是一个用于开发由语言模型驱动的应用程序的框架。它提供了一套工具和抽象，使开发者能容易地构建复杂的应用程序。LangChain是应用程序框架。提供了工具和抽象，能够更容易构建复杂应用。"

# demo1：禁用分隔符优先，按固定字节数分割
splitter_1 = CharacterTextSplitter(
    chunk_size=40,  # 分割块大小
    chunk_overlap=5,  # 块间重叠字符数
    separator=""  # 禁用分隔符优先
)
texts = splitter_1.split_text(text)
for i, chunk in enumerate(texts):
    print(len(chunk))
    print(chunk)
print("-"*50)

# demo2：按句号优先分割，其次考虑块大小，将相邻分割合并
splitter_2 = CharacterTextSplitter(
    chunk_size=40,   # 每个块的最大字符数
    chunk_overlap=5, # 块之间的重叠字符数
    separator="。",  # 按句号分割优先
    # keep_separator=True,  # 是否保留分割符
)
chunks = splitter_2.split_text(text)
for  i,chunk in enumerate(chunks):
    print(len(chunk))
    print(chunk)


