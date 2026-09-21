
from langchain.agents import create_agent
from langchain.agents.middleware import ModelFallbackMiddleware
from langchain.messages import HumanMessage

# 中间件作用：模型备用切换

agent = create_agent(
    model="ollama:fake_model",
    middleware=[
        ModelFallbackMiddleware(
            "ollama:gpt-oss:20b",
            "ollama:deepseek-r1:14b",
        ),
    ],
)

response = agent.invoke({"messages": [HumanMessage("hi")]})
print(response["messages"][-1].response_metadata.get("model_name"))