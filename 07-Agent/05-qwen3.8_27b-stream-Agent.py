# Agent的流式输出

from typing import Any
from rich import print as rprint
from langchain.tools import tool
from langgraph.config import get_stream_writer
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

@tool
def query_customer_data(customer_id: str) -> dict[str, Any]:
    """
    查询客户基本信息

    Args:
        customer_id: 客户ID，用于唯一标识客户

    Returns:
        包含客户基本信息的字典，如姓名、等级、加入日期等
    """
    # 模拟数据库查询
    return {"name": "张三","level": "VIP","join_date": "2023-01-15"}

@tool
def check_order_history(customer_id: str) -> dict[str, Any]:
    """
    查询客户订单历史

    Args:
        customer_id: 客户ID，用于唯一标识客户

    Returns:
        包含客户订单历史的字典，如总订单数、总花费等
    """
    return {"total_orders": 15,"total_spent": 25800.00}

@tool
def get_current_promotions() -> dict[str, Any]:
    """
    获取当前可用促销活动

    Returns:
        包含当前可用促销活动的字典，如活动名称、有效日期等
    """
    return {
        "promotions": ["老用户优惠", "会员专属折扣"],
        "valid_until": "2027-01-31"
    }

@tool
def generate_sales_report() -> str:
    """生成销售报告"""
    writer = get_stream_writer()
    writer({"type": "生成销售报告", "message": "开始生成销售报告"})
    for i in range(1, 4):
        writer({"type": "生成销售报告","message": f"生成销售报告进度百分比：{i * 25}%"})
    writer({"type": "生成销售报告", "message": "报告生成完成"})
    return f"销售报告：总收入150万元，同比增长12%"

@tool
def generate_inventory_report() -> str:
    """生成库存报告"""
    writer = get_stream_writer()
    writer("开始库存分析...")
    writer("检查当前库存量...")
    writer("生成库存报告...")
    return "当前库存量为10000件，库存充足"

agent = create_agent(
    model= "ollama:qwen3.8:27b",
    tools=[query_customer_data, check_order_history, get_current_promotions],
)

# checkpointer = InMemorySaver()
checkpoints_agent = create_agent(
    model= "ollama:qwen3.8:27b",
    tools=[query_customer_data, check_order_history, get_current_promotions],
    checkpointer=InMemorySaver(),
)

reporting_agent = create_agent(
    model="ollama:qwen3.8:27b",
    tools=[generate_sales_report, generate_inventory_report],
)

# 1. 流式输出模式 values：逐步输出完整历史信息
for chunk in agent.stream(
    {"messages" : [{"role":"user","content":"查询客户id为cust1234的完整的信息、历史订单和可用优惠"}]},
    stream_mode="values"
): rprint(chunk)

# 2. 流式输出模式 updates：默认模式，逐步输出增量信息
for chunk in agent.stream(
    {"messages" : [{"role":"user","content":"查询客户id为cust1234的完整的信息、历史订单和可用优惠"}]},
    stream_mode="updates"
): rprint(chunk)

# 3. 流式输出模式 messages：打字机式逐 token输出
for chunk in agent.stream(
    {"messages" : [{"role":"user","content":"查询客户id为cust1234的完整的信息、历史订单和可用优惠"}]},
    stream_mode="messages"
): print(chunk[0].content,end="",flush=True)

# 4. 流式输出模式 tasks：通过显示时间，监控生命周期
for chunk in agent.stream(
    {"messages" : [{"role":"user","content":"查询客户id为cust1234的完整的信息、历史订单和可用优惠"}]},
    stream_mode="tasks"
): rprint(chunk)

# 5. 流式输出模式 debug：tasks plus，更详细
for chunk in agent.stream(
    {"messages" : [{"role":"user","content":"查询客户id为cust1234的完整的信息、历史订单和可用优惠"}]},
    stream_mode="debug"
): rprint(chunk)

# 6. 流式输出模式 checkpoints：检查点追踪
for chunk in checkpoints_agent.stream(
    {"messages" : [{"role":"user","content":"查询客户id为cust1234的完整的信息、历史订单和可用优惠"}]},
    stream_mode="checkpoints",
    config={"configurable": {"thread_id": "session01"}},
): print(chunk)

# 7. 流式输出模式 custom：显示进度信息
for chunk in reporting_agent.stream(
    {"messages": ["生成销售报告和库存报告"]},
    stream_mode="custom"
): print(chunk)

# 8. 混合输出模式 ：组合基础输出模式，拥有多模式特征
for chunk in agent.stream(
    {"messages" : [{"role":"user","content":"查询客户id为cust1234的完整的信息、历史订单和可用优惠"}]},
    stream_mode=["tasks","updates"],
): rprint(chunk)



