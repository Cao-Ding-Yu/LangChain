# 指数退避算法设置模型调用失败的重试策略

from langchain.messages import HumanMessage
from langchain.agents import create_agent
from langchain.agents.middleware import ModelRetryMiddleware

agent_1 = create_agent(
    model="ollama:gpt-fake:20b",
    middleware=[
        ModelRetryMiddleware(
            max_retries=2, # 最大重试次数（不含初始调用）
            retry_on= (Exception,), # 针对特定的异常时触发重试
            on_failure="continue", # 达到最大重试次数后的行为：['continue','error',自定义函数]
            backoff_factor=2.0, # 指数退避因子
            initial_delay=1.0, # 初始等待秒数
            max_delay=10.0, # 最大重试等待上限
            jitter=True, # 开启抖动（在等待时间区间中加入随机性）
        ),
    ],
)

agent_2 = create_agent(
    model="ollama:gpt-fake:20b",
    middleware=[
        ModelRetryMiddleware(
            max_retries=2, # 最大重试次数（不含初始调用）
            retry_on= (Exception,), # 针对特定的异常时触发重试
            on_failure="error", # 达到最大重试次数后的行为：['continue','error',自定义函数]
            backoff_factor=2.0, # 指数退避因子
            initial_delay=1.0, # 初始等待秒数
            max_delay=10.0, # 最大重试等待上限
            jitter=True, # 开启抖动（在等待时间区间中加入随机性）
        ),
    ],
)

# 测试 1: on_failure="continue"
response = agent_1.invoke({"messages": [HumanMessage("1+1=?")]})
for msg in response["messages"]: msg.pretty_print()

# 测试 2: on_failure="error"
response = agent_2.invoke({"messages": [HumanMessage("1+1=?")]})
for msg in response["messages"]: msg.pretty_print()

