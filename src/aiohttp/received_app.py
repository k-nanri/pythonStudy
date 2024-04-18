from fastapi import FastAPI
import requests
import aiohttp
from logging import getLogger

logger = getLogger(__name__)
logger.info("message")

app = FastAPI()


@app.get("/task2")
async def get_task2():

    print("Received Request!!")
    response = requests.get("http://127.0.0.1:8000")
    print(response.status_code)
    return {"res": response.json()}


@app.get("/task1")
async def get_task1():

    print("Received Request!!")
    response = requests.get("http://127.0.0.1:8000")
    print(response.status_code)
    return {"res": response.json()}
    # async with aiohttp.ClientSession() as session:
    #    response = await session.get("http://127.0.0.1:8000")
    #    json_res = await response.json()
    #    return {"res": json_res}


# uvicorn received_app:app --port 8001
