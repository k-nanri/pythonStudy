from fastapi import BackgroundTasks, FastAPI
import time
from logging import getLogger
import uuid
from uuid import UUID
from typing import Union
import asyncio
from pydantic import BaseModel

logger = getLogger("uvicorn.app")
app = FastAPI()

collecting_status = []


class CollectRequest(BaseModel):
    mode: str


@app.get("/colect2")
async def collect2():
    logger.info("Start collect2")


@app.get("/collect_status/{request_id}")
async def collect_status(request_id, query: Union[str, None] = None):
    logger.info("Start collect_status")
    status = "complete"
    logger.info("current collecting_status=" + str(collecting_status))
    for item in collecting_status:
        if item["request_id"] == request_id:
            status = "collecting"
            break

    logger.info("End collect_status")
    response = {"status": status}
    return response


async def execute_long_time(mode: str, request_id: str):
    logger.info("Start execute_long_time method")
    logger.info("execute_log_time param mode=" + mode + ", request_id=" + request_id)
    collecting_status.append({"request_id": request_id, "status": "collecting"})
    await asyncio.sleep(60)

    if {"request_id": request_id, "status": "collecting"} in collecting_status:
        collecting_status.remove({"request_id": request_id, "status": "collecting"})

    logger.info("End execute_long_time method")


@app.post("/collectlog")
async def collect_log(request: CollectRequest, background_tasks: BackgroundTasks):
    request_id = uuid.uuid4()
    background_tasks.add_task(execute_long_time, request.mode, str(request_id))

    response = {"request_id": request_id}
    return response


"""
@app.post("/send-notification/{mode}")
async def send_notification(mode: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(execute_long_time, mode, message="notification")
    return {"message": "Notification sent in the background"}
"""

# 起動
# uvicorn backgroundtask:app --reload
