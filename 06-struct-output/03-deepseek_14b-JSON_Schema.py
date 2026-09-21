
from langchain_ollama import ChatOllama

model = ChatOllama(
    model="deepseek-r1:14b",
    # base_url="http://localhost:11434",
)

# 手动定义json结构
json_schema = {
    "title": "MovieInfo",
    "description": "包含电影名称、上映年份、导演、演员和评分的电影对象",
    "type": "object",
    "properties": {
        "title": {"type": "string", "description": "电影名称"},
        "year": {"type": "integer", "description": "上映年份"},
        "director": {"type": "string", "description": "导演"},
        "cast": {  # 嵌套数组
            "type": "array",
            "description": "演员列表",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "演员姓名"},
                    "role": {"type": "string", "description": "演员角色"}
                },
                "required": ["name", "role"]
            }
        },
        "rating": {"type": "number", "description": "评分"}
    },
    "required": ["title", "year", "director", "cast", "rating"]
}

structured_model = model.with_structured_output(json_schema,method="json_schema")
print(structured_model.invoke("星际穿越的电影信息"))

