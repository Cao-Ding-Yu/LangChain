# 指数退避算法设置工具调用失败的重试策略

import datetime
from langchain_core.tools import tool
from langchain.messages import HumanMessage
from langchain.agents import create_agent
from langchain.agents.middleware import ToolRetryMiddleware, ToolCallLimitMiddleware

count = 0
start_time = None

@tool
def add(a:int, b:int):
    """计算两数之和"""
    global count
    count += 1
    global start_time
    current_time = datetime.datetime.now()
    interval = (current_time - start_time).total_seconds() if start_time is not None else 0
    result = f"第 {count} 次调用，当前时间： {current_time}, 和上次调用间隔 {interval} 秒"
    with open("09-call_times.txt", "a", encoding="utf-8") as f: f.write(result + "\n")
    start_time = current_time
    raise TimeoutError("Not Implemented")

agent = create_agent(
    model="ollama:gpt-oss:20b",
    tools=[add],
    middleware=[
        ToolRetryMiddleware( # 限制单次模型调用的重试次数
            max_retries=6,  # 最大重试次数（不含初始调用）
            tools=[add], # 指定应用策略的函数
            retry_on=(TimeoutError,),  # 针对特定的异常时触发重试
            on_failure="continue",  # 达到最大重试次数后的行为：['continue','error',自定义函数]
            backoff_factor=2.0,  # 指数退避因子
            initial_delay=1.0,  # 初始等待秒数
            max_delay=10.0,  # 最大重试等待上限
            jitter=False,  # 开启抖动（在等待时间区间中加入随机性）
        ),
        ToolCallLimitMiddleware( # 限制只产生一次模型调用请求
            run_limit=1,  # 限制单次运行总调用次数
            exit_behavior="continue",  # 处理行为
        ),
    ],
)

# 1. 提问 -> 2. 决定调用工具 -> 3. 重试失败后错误反馈 -> 4. 最终给出的兜底回复
response = agent.invoke({"messages": [HumanMessage("调用工具计算1+1=?")]})
for msg in response["messages"]: msg.pretty_print()