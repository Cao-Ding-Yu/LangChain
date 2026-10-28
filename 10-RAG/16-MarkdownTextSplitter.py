# Markdown切分器

from langchain_text_splitters import MarkdownTextSplitter

markdown_text = """
# 第一章 简介
这是第一章的正文内容，用于测试 Markdown 切分效果。
## 1.1 节
这是 1.1 节的正文，包含一些普通文字。
```python
def hello():
    print("Hello Markdown")
"""

splitter = MarkdownTextSplitter(
    chunk_size=30,
    chunk_overlap=0,
    is_separator_regex=True, # 识别正则表达式内容
)

docs = splitter.create_documents([markdown_text])
for doc in docs: print(f"🔍分块:" + doc.page_content)

