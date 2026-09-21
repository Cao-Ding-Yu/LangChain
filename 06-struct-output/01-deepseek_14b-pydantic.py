
from enum import StrEnum
from typing import Literal
from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field, ValidationError

model = ChatOllama(
    model="deepseek-r1:14b",
    # base_url="http://localhost:11434",
)

class Job(StrEnum):
    """职业枚举"""
    Programmer = "程序员"
    Farmer = "农民"
    Teacher = "教师"

class Address(BaseModel):
    """家庭住址子嵌套"""
    city : str = Field(description="城市")

class Person(BaseModel):
    """个人信息"""
    name : str = Field("佚名",description="姓名") # 1. 设置字段的默认值 default (部分厂商不支持)
    sex : Literal['男','女'] = Field(description="性别") # 2. 单个枚举类型：使用 Literal[] 或创建 StrEnum class
    weight: int | None = Field(description="体重")  # 3. 可选字段：等同于 weight : Optional[int]，未知则返回 None
    occupation: list[Job] = Field(description="工作职业")  # 4. 列表提取 list[]
    address: Address = Field(description="家庭住址") # 5. 嵌套结构：Address嵌套进 Person
    age: int = Field(description="年龄", le=35) # 6. 限制条件测试：程序报错或模型自动修改不合法内容

class PersonList(BaseModel):
    """人员列表信息"""
    people : list[Person] = Field(description="人员列表")

if __name__ == "__main__":
    try:
        structured_model = model.with_structured_output(PersonList)
        print(structured_model.invoke("王伟是一个家住吉林市体重180斤的女农民，李明是一个家住长春市的男教师兼程序员，两人的年龄分别为30岁和40岁"))
    except ValidationError as e: print(e)

