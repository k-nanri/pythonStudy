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


async def send(name):
    logger.info("--- " + name + " -----")
    cnt = 0
    while True:
        async with aiohttp.ClientSession() as session:
            cnt += 1
            url = "http://127.0.0.1:8000/collectlog"
            resp = await session.post(url, json={"mode": "all"})
            if resp.status == 200:
                logger.info("Send request count=" + str(cnt))
            else:
                logger.error("Send Failed!!")

            if cnt == 1000:
                break


async def main():
    task1 = asyncio.create_task(send("task1"))
    # task2 = asyncio.create_task(send("task2"))
    await task1
    # await task2


asyncio.run(main())
