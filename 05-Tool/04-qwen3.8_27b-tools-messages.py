# 多工具调用

from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langchain_core.utils.function_calling import convert_to_openai_tool
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

# 部分AI不支持并行工具调用，一次 AIMessage只能指出使用一个工具

model = ChatOllama(
    model="qwen3.8:27b",
    # base_url="http://localhost:11434",
)

# 股票查询工具
@tool(parse_docstring=True)
def get_stock_price(company: str, timeframe: str = "today") -> str:
    """
    获取指定公司的股票价格信息

    Args:
        company: 公司名称（如：苹果公司, 微软公司, 谷歌公司）
        timeframe: 时间范围（today-今日, week-本周, month-本月）
    """
    mock_data = { # 虚拟股票数据
        "苹果公司": {"today": 185.20, "week": 183.50, "month": 180.75},
        "微软公司": {"today": 415.86, "week": 412.30, "month": 405.42},
        "谷歌公司": {"today": 15.42, "week": 15.20, "month": 14.85}
    }

    if company in mock_data:
        price = mock_data[company].get(timeframe, "未知时间范围")
        return f"{company} {timeframe}价格: {price}美元"
    else: return f"未找到股票代码 {company} 的数据"

# 新闻搜索工具
@tool(parse_docstring=True)
def search_news(company: str) -> str:
    """
    搜索指定公司的财经新闻

    Args:
        company: 公司名称

    Returns:
        公司的财经新闻，每个新闻占一行
    """
    mock_news = { # 虚拟新闻数据
        "苹果公司": [
            "苹果发布新款iPhone，股价上涨3%",
            "苹果与欧盟达成反垄断和解协议",
            "苹果将在印度扩大生产规模"
        ],
        "微软公司": [
            "微软Azure云业务季度增长超预期",
            "微软完成对Nuance的收购",
            "微软推出新一代AI助手Copilot"
        ],
        "谷歌公司": [
            "谷歌发布新AI模型，性能提升20%",
            "谷歌与OpenAI合作，开发新的AI助手",
            "谷歌在欧洲展开AI研究项目"
        ]
    }
    news_list = mock_news.get(company, [f"未找到{company}的相关新闻"])
    return "\n".join(news_list)

# rprint(convert_to_openai_tool(search_news))
# rprint(convert_to_openai_tool(get_stock_price))

# 1. 模型绑定工具(tool_choice:none表示不使用，auto表示自适应，required表示使用，函数名则为指定使用函数)
model_with_tools = model.bind_tools([get_stock_price, search_news], tool_choice="auto")

# 2. 消息列表初始化(选一)
message_list = list([
    HumanMessage(content="苹果公司今天的股价是多少？最近有什么新闻？"),
    # HumanMessage(content="比较一下微软和苹果的股价"),
    # HumanMessage(content="腾讯最近有什么重大新闻？"),
    # HumanMessage(content="海水为什么是咸的？"),
])

# user -> ai
response = model_with_tools.invoke(message_list)
message_list.append(response)

# user -> ai -> tool
for tool_call in response.tool_calls:
    if tool_call["name"] == "get_stock_price":
        message_list.append(get_stock_price.invoke(tool_call))
    if tool_call["name"] == "search_news":
        message_list.append(search_news.invoke(tool_call))

# user -> ai -> tools -> ai
message_list.append(model.invoke(message_list))

for msg in message_list:
    msg.pretty_print()