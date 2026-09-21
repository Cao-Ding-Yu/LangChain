
from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

model = ChatOllama(
    model="gpt-oss:20b",
    # base_url="http://localhost:11434",
)

name = "小李"
user_input = "你叫什么名字"

# 创建方式 1
chat_prompt_template_temp = ChatPromptTemplate(["解释什么是Python"])

# 创建方式 2 (推荐)
chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system","你是一个Python高级程序员，你的名字叫{name}"), # 参数类型 1：元组
    "你很精通Python吗", # 参数类型 2：字符串，默认身份为 Human
    AIMessage("是的"), # 参数类型 3：消息对象
    HumanMessagePromptTemplate.from_template("{user_input}"), # 参数类型 4：BaseMessagePromptTemplate，相比BaseMessage增加赋值{xx}变量作用
    {"role":"ai","content":"{name}"}, # 参数类型 5：字典
    chat_prompt_template_temp, # 参数类型 6：ChatPromptTemplate
])

# 根据模板生成输入内容
result = chat_prompt_template.invoke({"name":name,"user_input":user_input}) # 方式 1：invoke，返回 ChatPromptTemplate (推荐)
result_str = chat_prompt_template.format(name=name, user_input=user_input) # 方式 2：format，返回字符串
result_list = chat_prompt_template.format_messages(name=name, user_input=user_input) # 方式 3：format_messages，返回消息列表

print(result_str)
print(model.invoke(result).content)



