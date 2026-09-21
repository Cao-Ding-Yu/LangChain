
from pydantic import BaseModel, Field
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

model = ChatOllama(
    model="deepseek-r1:14b",
    # base_url="http://localhost:11434",
)
# ---------------------------
# -----旧式输出版本，已弃用------
# ---------------------------

# 1. 创建提示词模板
prompt_template = ChatPromptTemplate.from_messages([
    ("system","回答用户问题,必须始终输出一个包含title(电影标题)和year(上映年份)的JSON对象"),
    ("human","问题：{question}")
])

# 2. 创建输出解析器
class Movie(BaseModel):
    title: str = Field(description="电影名称")
    year: int = Field(description="上映年份")
parser = JsonOutputParser(pydantic_object=Movie)

# 3. 方式 1：创建链，调用链
chain = prompt_template | model | parser
response = chain.invoke({"question": "介绍电影盗梦空间"})

# 3. 方式 2：直接嵌套调用
# response = parser.invoke(model.invoke(prompt_template.invoke({"question": "介绍电影《盗梦空间》"})))

# 4. 打印结果
print(response)