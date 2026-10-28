# 异步调用

import asyncio
from langchain_ollama import ChatOllama

model = ChatOllama(
    model="deepseek-r1:14b",
    # base_url="http://localhost:11434",
)

questions = ["美国首都在哪", "中国首都在哪"]

async def async_ainvoke():
    tasks = [asyncio.create_task(model.ainvoke(q)) for q in questions]

    for coro in asyncio.as_completed(tasks):
        response = await coro
        print(response.content)

async def async_abatch():
    batch_task = asyncio.create_task(model.abatch(questions))

    for i in range(3):
        await asyncio.sleep(1)

    responses = await batch_task
    for response in responses:
        print(response.content)

async def async_gather():
    tasks = [asyncio.create_task(model.ainvoke(q)) for q in questions]

    async def wait_and_print():
        for coro in asyncio.as_completed(tasks):
            response = await coro
            print(response.content)

    async def other_work():
        for i in range(3):
            await asyncio.sleep(1)
            print(f"其他工作已进行 {i+1} 秒")

    await asyncio.gather(wait_and_print(), other_work())

if __name__ == "__main__":
    # asyncio.run(async_ainvoke())
    # asyncio.run(async_abatch())
    asyncio.run(async_gather())

