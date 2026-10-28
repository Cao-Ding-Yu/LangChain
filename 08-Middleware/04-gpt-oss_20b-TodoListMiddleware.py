# 中间件作用：任务拆解

import subprocess
from pathlib import Path
from rich import print as rprint
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain.agents.middleware import TodoListMiddleware

WORKSPACE = Path("04-workspace")

@tool
def list_files(path: str = ".") -> str:
    """
    列出工作区指定目录下的文件和子目录(path为相对路径)

    Args:
        path: 工作区下的相对路径，一定指向目录，默认为.，表示工作区根路径，不能访问工作区外的目录
    """
    target = (WORKSPACE / path).resolve()

    if not str(target).startswith(str(WORKSPACE.resolve())): return "错误：只允许访问工作区内的目录。"
    if not target.exists(): return f"错误：目录不存在: {path}"
    if not target.is_dir(): return f"错误：不是目录: {path}"
    items = sorted(target.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
    if not items: return f"目录为空: {path}"

    lines = list()
    for item in items:
        rel = item.relative_to(WORKSPACE.resolve())
        kind = "[DIR]" if item.is_dir() else "[FILE]"
        lines.append(f"{kind} {rel.as_posix()}")
    return "\n".join(lines)

@tool
def read_file(path: str) -> str:
    """
    读取工作区中的文本文件内容(path为相对路径)

    Args:
        path: 工作区内的文件名
    """
    file_path = (WORKSPACE / path).resolve()
    if not str(file_path).startswith(str(WORKSPACE.resolve())): return "错误：只允许读取工作区内的文件。"
    if not file_path.exists(): return f"错误：文件不存在: {path}"
    return file_path.read_text(encoding="utf-8")

@tool
def write_file(path: str, content: str) -> str:
    """
    写入工作区中的文本文件(path为相对路径)

    Args:
        path: 工作区内的文件名
        content: 写入文件的内容
    """
    file_path = (WORKSPACE / path).resolve()
    if not str(file_path).startswith(str(WORKSPACE.resolve())): return "错误：只允许写入工作区内的文件。"
    file_path.write_text(content, encoding="utf-8")
    return f"已写入文件: {path}"

@tool
def run_tests() -> str:
    """
    在工作区运行 pytest -q，并返回输出。
    不接收任何参数，返回格式为
    returncode=0|1
    STDOUT:
    STDERR:
    """
    try:
        result = subprocess.run(
            ["pytest", "-q"],
            cwd=str(WORKSPACE),
            capture_output=True,
            text=True,
            timeout=10,
        )
        return (
            f"returncode={result.returncode}\n\n"
            f"STDOUT:\n{result.stdout}\n\n"
            f"STDERR:\n{result.stderr}"
        )
    except Exception as e:
        return f"运行测试失败: {e}"

# 智能体创建
agent = create_agent(
    model= "ollama:gpt-oss:20b",
    tools=[list_files, read_file, write_file, run_tests],
    middleware=[TodoListMiddleware()],
    system_prompt="你是一个代码修复助手。遇到多步骤任务时，先使用write_todos制定待办事项，然后读取文件、修复代码并运行测试。工作全部在工作区下进行。"
)

# 结果打印
response = agent.invoke({"messages" : [HumanMessage("测试并修复工作区下的my_add.py文件中的代码")]})
rprint(response)