# 模型执行时钩子函数

from typing import Callable
from langchain.agents.middleware import ModelRequest, ModelResponse, AgentMiddleware
from langchain_core.messages import HumanMessage
from langchain.agents import create_agent

class WrapModelCallMiddleware(AgentMiddleware):
    def wrap_model_call(self, request: ModelRequest, handler: Callable[[ModelRequest], ModelResponse]) -> ModelResponse:
        request.messages[-1].content += "---> wrap_model_call_before <---"
        response = handler(request)
        response.result[0].content += "---> wrap_model_call_after <---"
        return response

agent = create_agent(
    model="ollama:gpt-oss:20b",
    middleware=[WrapModelCallMiddleware()],
)

response = agent.invoke({"messages": [HumanMessage("说你好")]})
for msg in response["messages"]:msg.pretty_print()