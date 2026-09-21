
import re
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain.agents.middleware import PIIMiddleware

# 中间件作用：敏感信息隐藏

# 自定义手机号匹配规则
def detect_phone_number(content: str):
    return [
        {
            "text": m.group(0), # 匹配到的11位完整数字文本
            "start": m.start(), # 数字在原文本中的起始索引位置
            "end": m.end() # 数字在原文本中的结束索引位置
        } for m in re.finditer(r"[0-9]{11}", content)
    ]

agent = create_agent(
    model= "ollama:gpt-oss:20b",
    middleware=[ # 屏蔽敏感个人信息 (默认包括：邮件、银行卡号、url地址、mac地址、ip地址，自定义包括：手机号，api_key)
        # strategy : Literal["block":报错, "redact":字段代替, "mask":部分遮挡, "hash":转为哈希]
        PIIMiddleware("email",strategy="redact",apply_to_input=True),
        PIIMiddleware("credit_card",strategy="mask",apply_to_input=True),
        PIIMiddleware("url",strategy="hash",apply_to_input=True),
        PIIMiddleware("mac_address",strategy="mask",apply_to_input=True),
        PIIMiddleware("ip",strategy="block",apply_to_input=True),
        PIIMiddleware("phone_number", strategy="mask", apply_to_input=True, detector=detect_phone_number),
        PIIMiddleware("api_key", strategy="hash", apply_to_input=True, detector=r"sk-[a-zA-Z0-9]+"),
    ], # 输入时启用：apply_to_input = True, 输出时启用：apply_to_output = False, 工具调用时启用：apply_to_tool_results = False
)

# 测试 1
response = agent.invoke({
        "messages" : [
            HumanMessage("""帮我向 843941787@qq.com 发送一封邮件，同时查看银行卡号： 5105-1051-0510-5100 的余额，访问 https://localhost:12345，确认这是不是 MAC地址： 11-11-11-11-11-11，这是不是有效的 API_KEY： sk-awef23AFEfaafaefa，帮我给这个号码打电话： 12345612345"""),
        ]
    }
)
for msg in response["messages"]: msg.pretty_print()

# 测试 2
try: agent.invoke({"messages": [HumanMessage("这IP能不能ping通：192.168.10.1")]})
except Exception as e: print(f"检测到ip，抛出异常{e}")