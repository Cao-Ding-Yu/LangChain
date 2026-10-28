# token文本切分器

from langchain_text_splitters import TokenTextSplitter, CharacterTextSplitter

text = "人工智能是一个强大的开发框架。它支持多种语言模型和工具链。人工智能是指通过计算机程序模拟人类智能的一门科学。自20世纪50年代诞生以来，人工智能经历了多次起伏。"

splitter_1 = TokenTextSplitter(
    chunk_size=30,  # 单块最大token数
    chunk_overlap=0,  # 重叠token数
    # model_name="gpt-4", # 选择模型映射的编码器
    encoding_name="cl100k_base",  # 直接指定编码器
)
texts = splitter_1.split_text(text)
for i, chunk in enumerate(texts):
    print(len(chunk))
    print(chunk)
print("-" * 50)

splitter_2 = CharacterTextSplitter.from_tiktoken_encoder(
    encoding_name="cl100k_base", # 指定编码器
    chunk_size=20,  # 块最大token数
    chunk_overlap=0,  # 块重叠token数
    separator="。",  # 指定分隔符
    keep_separator=False,  # 是否保留分隔符
)
texts = splitter_2.split_text(text)
for chunk in texts:
    print(len(chunk))
    print(chunk)
print("-" * 50)

