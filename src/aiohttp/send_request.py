import aiohttp
import asyncio

# 非同期にリクエストを送信したい。


async def main():
    async with aiohttp.ClientSession() as session:
        for i in range(0, 5):
            print("Send!!")
            resp = session.get("http://127.0.0.1:8001")
            # print(resp.status)
            # print(await resp.text())

        await resp.text()


asyncio.run(main())
