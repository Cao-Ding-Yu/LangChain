# 使用typeddict实现结构化输出

from rich import print as rprint
from langchain_ollama import ChatOllama
from typing_extensions import TypedDict, Annotated

model = ChatOllama(
    model="deepseek-r1:14b",
    # base_url="http://localhost:11434",
)

# 1. 基础创建方式
class Actor(TypedDict):
    name : str
    role : str

# 2. 高级创建方式
# Annotated[数据类型,附加说明1,附加说明2,附加说明n]
# 其中 ... 意味着字段不可省略，部分模型不支持
class Movie(TypedDict):
    title : Annotated[str,...,"电影名"]
    year : Annotated[int,...,"上映时间"]
    director : Annotated[str,...,"导演"]
    rating : Annotated[float,...,"评分"]
    cast : Annotated[list[Actor],"演员列表"]

# 加入 include_raw = True会显示完整 AIMessage，其中 parsed字段是结果
structured_model = model.with_structured_output(Movie, include_raw=True)
rprint(structured_model.invoke("介绍电影星际穿越"))