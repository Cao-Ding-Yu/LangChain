# 模板的基本使用

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

model = ChatOllama(
    model="gpt-oss:20b",
    # base_url="http://localhost:11434",
)

base_template_ = ChatPromptTemplate.from_messages([
    ("system", "你是{department}的{role}"),
    ("user", "{task}")
])

# 基本模板
class PromptLibrary:
    same_template_1 = ChatPromptTemplate.from_messages([
        ("system", "你是{department}的{role}"),
        ("user", "{task}")
    ])
    same_template_2 = ChatPromptTemplate.from_messages([
        ("system", "你是{department}的{role}"),
        ("user", "{task}")
    ])

# 财务部门模板
finance_template = PromptLibrary.same_template_1.partial(department="财务部门", role="财务总监")
# IT部门模板
it_template = PromptLibrary.same_template_1.partial(department="IT部门", role="技术负责人")
# 销售部门模板
sales_template = PromptLibrary.same_template_2.partial(department="销售部门", role="销售顾问")

# 财务部门使用
finance_input = sales_template.invoke({"task":"你是谁"})
print(model.invoke(finance_input).content)

# IT部门使用
it_input = it_template.invoke({"task":"你是谁"})
print(model.invoke(it_input).content)

# 销售部门使用
sales_input = sales_template.invoke({"task":"你是谁"})
print(model.invoke(sales_input).content)

