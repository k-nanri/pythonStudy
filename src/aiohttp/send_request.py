import aiohttp
import asyncio
import logging
from logging import getLogger, StreamHandler, Formatter

logger = getLogger("LogTest")
logger.setLevel(logging.DEBUG)
stream_handler = StreamHandler()
stream_handler.setLevel(logging.DEBUG)
handler_format = Formatter("%(asctime)s - %(message)s")
stream_handler.setFormatter(handler_format)
logger.addHandler(stream_handler)

# 非同期にリクエストを送信したい。


async def send(name):
    logger.info("--- " + name + " -----")
    async with aiohttp.ClientSession() as session:
        logger.info("--- " + name + " Send!!")
        url = "http://127.0.0.1:8001/" + str(name)
        resp = await session.get(url)
        logger.info("--- " + name + " status = " + str(resp.status))
        logger.info("--- " + name + str(await resp.text()))


async def main():
    task1 = asyncio.create_task(send("task1"))
    task2 = asyncio.create_task(send("task2"))
    await task1
    await task2


asyncio.run(main())
