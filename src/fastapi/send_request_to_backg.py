from fastapi import FastAPI
from logging import getLogger
from pydantic import BaseModel
import aiohttp
import asyncio

logger = getLogger("uvicorn.app")
app = FastAPI()


class CollectRequest(BaseModel):
    mode: str


class CollectResponse(BaseModel):
    request_id: str


class CollectStatusResponse(BaseModel):
    status: str


@app.post("/collectlog")
async def collectlog(request: CollectRequest):
    logger.info("Start collectlog method")
    async with aiohttp.ClientSession() as session:
        url = "http://localhost:8000/collectlog"
        request_json = request.model_dump_json()
        response = await session.post(url, json={"mode": "all"})
        if response.status != 200:
            logger.error("Failed to response = " + str(response.json()))
            return {"message": "Failed to error."}

        response_json = CollectResponse(**(await response.json()))
        request_id = response_json.request_id

        cnt = 0
        while True:
            url = "http://localhost:8000/collect_status/" + request_id
            logger.info("Request to collect status.")
            response = await session.get(url)
            if response.status != 200:
                logger.error("Failed to status")
                raise Exception("Failed to status")

            response_json = CollectStatusResponse(**(await response.json()))
            logger.info("response = " + str(response_json.status))
            if response_json.status == "complete":
                logger.info("Status is complete")
                break
            else:
                await asyncio.sleep(5)
                cnt += 1

            if cnt == 10:
                raise Exception("Failed to collect")

    logger.info("End collectlog method")
    return {"status": "finish"}
