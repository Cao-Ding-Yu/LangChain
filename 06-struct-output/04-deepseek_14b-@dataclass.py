
from pydantic import Field
from dataclasses import dataclass
from langchain_ollama import ChatOllama

model = ChatOllama(
    model="deepseek-r1:14b",
    # base_url="http://localhost:11434",
)

@dataclass
class Movie:
    title: str = Field(description="电影名称")
    year: int = Field(description="上映年份")
    director: str = Field(description="导演")
    rating: float = Field(description="评分")

# 部分模型厂商不支持 @dataclass
structured_model = model.with_structured_output(Movie)
print(structured_model.invoke("电影盗梦空间的信息"))

