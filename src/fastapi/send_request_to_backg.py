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


@app.post("/collectlog")
async def collectlog(request: CollectRequest):
    logger.info("Start collectlog method")
    async with aiohttp.ClientSession as session:
        url = "http://localhost:8000/collectlog"
        response = await session.post(url, request)
        if response.status != 200:
            logger.error("Failed to response")
            return {"message": "Failed to error."}

        response_json = CollectResponse(response.json())
        request_id = response_json.request_id

        while True:
            url = "http://localhost:8000/collect_status/" + request_id

    logger.info("End collectlog method")
