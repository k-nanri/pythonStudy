from fastapi import FastAPI
import requests
import aiohttp
import logging
from logging import getLogger, StreamHandler, Formatter

logger = getLogger("LogTest")
logger.setLevel(logging.DEBUG)
stream_handler = StreamHandler()
stream_handler.setLevel(logging.DEBUG)
handler_format = Formatter("%(asctime)s - %(message)s")
stream_handler.setFormatter(handler_format)
logger.addHandler(stream_handler)

app = FastAPI()


@app.get("/task2")
async def get_task2():

    logger.info("Received task2 Request!!")
    # response = requests.get("http://127.0.0.1:8000")
    # logger.info("Send task2 response")
    # return {"res": response.json()}
    async with aiohttp.ClientSession() as session:
        response = await session.get("http://127.0.0.1:8000")
        json_res = await response.json()
        logger.info("Send task2 response")
        return {"res": json_res}


@app.get("/task1")
async def get_task1():

    logger.info("Received task1 Request!!")
    # response = requests.get("http://127.0.0.1:8000")
    # logger.info("Send task1 response")
    # return {"res": response.json()}
    async with aiohttp.ClientSession() as session:
        response = await session.get("http://127.0.0.1:8000")
        json_res = await response.json()
        logger.info("Send task1 response")
        return {"res": json_res}


# uvicorn received_app:app --port 8001
