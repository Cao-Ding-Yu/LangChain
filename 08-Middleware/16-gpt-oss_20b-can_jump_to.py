
from typing import Any
from langchain.agents import create_agent
from langchain.agents.middleware import hook_config, AgentState, AgentMiddleware
from langchain.messages import AIMessage, SystemMessage, HumanMessage
from langchain.tools import tool
from langgraph.runtime import Runtime

@tool(description="获取当日新闻")
def get_news() -> str:
    return f"美加墨世界杯今日开幕"

class MyMiddleware(AgentMiddleware):
    @hook_config(can_jump_to=["tools", "end"])
    def before_model(self, state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
        text = state["messages"][-1].content
        if isinstance(text, str) and "overflow" in text: # 假装内存溢出
            return {"messages": [AIMessage("上下文窗口溢出，终止")], "jump_to": "end"}
        if isinstance(text, str) and "direct tool" in text: # 跳转工具
            fake_tool_call = AIMessage(content="假消息", tool_calls=[{"name": "get_news", "args": {}, "id": "call_01"}])
            return {"messages": [fake_tool_call], "jump_to": "tools"}
        return None

    @hook_config(can_jump_to=["model"])
    def after_model(self, state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
        text = next((msg.content for msg in reversed(state["messages"]) if isinstance(msg, HumanMessage)),"")
        if isinstance(text, str) and "retry model" in text:
            if any(isinstance(msg.content, str) and "二次回答" in msg.content for msg in state["messages"]): return None
            return {"messages": [SystemMessage("打印'二次回答，你好'")],"jump_to": "model"}
        return None

agent = create_agent(
    model="ollama:gpt-oss:20b",
    tools=[get_news],
    middleware=[MyMiddleware()],
)

def run(user_input: str):
    result = agent.invoke({"messages": [{"role": "user", "content": user_input}]})
    for msg in result["messages"]: msg.pretty_print()

if __name__ == "__main__":
    # # Case 1: 直接跳 tools
    # print('=' * 30, '-> Case 1 <-', '=' * 30)
    # run("请帮我查今日新闻 direct tool")

    # Case 2: 输出后跳回 model
    print('=' * 30, '-> Case 2 <-', '=' * 30)
    run("请随便介绍一下 retry model")

    # # Case 3: 假装检测内存溢出而中断
    # print('=' * 30, '-> Case 3 <-', '=' * 30)
    # run("你好 overflow")
