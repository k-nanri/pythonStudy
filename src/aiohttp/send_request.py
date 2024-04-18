import aiohttp
import asyncio

# 非同期にリクエストを送信したい。


async def send(name):
    print("--- " + name + " -----")
    async with aiohttp.ClientSession() as session:
        print("--- " + name + " Send!!")
        resp = await session.get("http://127.0.0.1:8001")
        print("--- " + name + " status = " + str(resp.status))
        print("--- " + name + str(await resp.text()))


async def main():
    task1 = asyncio.create_task(send("task1"))
    task2 = asyncio.create_task(send("task2"))
    await task1
    await task2


asyncio.run(main())
