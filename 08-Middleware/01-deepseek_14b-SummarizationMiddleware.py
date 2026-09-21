
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

# 中间件作用：生成上下文摘要，减少上下文体量

model = ChatOllama(
    model="deepseek-r1:14b",
    profile={"max_input_tokens": 1000},
    # base_url="http://localhost:11434",
)

messages = [
    SystemMessage("你是个数学专家"),
    HumanMessage("你好，我是老王，你是谁？"),
    AIMessage("你好老王，我是小王"),
    HumanMessage("好的小王，很高兴认识你"),
    AIMessage("你高兴得太早了"),
    HumanMessage("呵呵，你什么意思")
]

agent = create_agent(
    model="ollama:deepseek-r1:14b",
    middleware=[
        SummarizationMiddleware(
            model=model, # 用于生成摘要的模型，一般选择较小模型以节省 token
            trigger=[ # 触发条件，满足其一即可
                ("tokens",100), # 消息最大 token数
                ("messages",6), # 最大消息数
                ("fraction",0.001) # 达到消息上限数占比 max_input_tokens * fraction
            ],
            keep=("messages",2), # 保留不被摘要的消息数(每种类消息都算一条)
            summary_prompt="对历史消息摘要，消息列表如下：{messages}" # 摘要提示词，必须含有 {messages}关键字
        )
    ]
)

response = agent.invoke({"messages": messages})
for msg in response["messages"]: msg.pretty_print()

