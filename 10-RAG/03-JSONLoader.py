# json加载器

from rich import print as rprint
from  langchain_community.document_loaders import JSONLoader

# 1. 提取全部数据
json_loader=JSONLoader(
    file_path="resources/03-load.json",
    jq_schema=".",  # 提取完整JSON对象
    text_content=False  # 标识非文本数据结构
)
rprint(json_loader.load())

# 2. 提取部分字符串数据
json_loader=JSONLoader(
    file_path="resources/03-load.json",
    # jq_schema=".status",
    # jq_schema=".status_list[]",
    jq_schema=".data.items[].content"
)
rprint(json_loader.load())

# 3. 提取部分非字符串数据
json_loader = JSONLoader(
    file_path='resources/03-load.json',
    jq_schema=".data.items[]",
    text_content=False,
)
rprint(json_loader.load())

# 4. 对象构造器
json_loader = JSONLoader(
    file_path='resources/03-load.json',
    text_content=False,
    jq_schema="""
        .data.items[] | {
            author,
            created_at,
            content: (.title + "\n" + .content)
        }
    """,
)
rprint(json_loader.load())

