
from langchain.agents import create_agent
from langchain.agents.middleware import FilesystemFileSearchMiddleware
from langchain.messages import HumanMessage

# 本地文件搜索与分析能力中间件

agent = create_agent(
    model="ollama:gpt-oss:20b",
    tools=[],  # 自动添加工具 Glob 和 Grep，分别用于目录读取和文件读取
    middleware=[
        FilesystemFileSearchMiddleware(
            root_path="04-workspace", # 搜索目录
            use_ripgrep=True, # 是否使用性能更快的 ripgrep
            max_file_size_mb=10, # 单个文件的最大体量（MB），防止内存耗尽
        ),
    ],
)

response = agent.invoke({"messages": [HumanMessage("生成目录下程序概述")]})
for msg in response["messages"]:msg.pretty_print()