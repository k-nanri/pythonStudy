import asyncio
import uuid
from logging import getLogger
from typing import List
import datetime

logger = getLogger("uvicorn.app")

from fastapi import (
    Depends,
    FastAPI,
    WebSocket,
    WebSocketDisconnect,
)
from pydantic import BaseModel, RootModel
from contextlib import asynccontextmanager


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def all_disconnect(self):
        logger.info("call all_disconnect")
        for connection in self.active_connections:
            logger.info("Call close")
            await connection.close()

    async def send_personal_message(
        self, message: dict[str, any], websocket: WebSocket
    ):
        await websocket.send_json(message)

    async def broadcast(self, message: dict[str, any]):
        for connection in self.active_connections:
            await connection.send_json(message)


manager = ConnectionManager()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Start up!!!")

    yield
    logger.info("Shutdown Start!!!")
    manager.all_disconnect()
    logger.info("Shutdown End  !!!")


app = FastAPI(lifespan=lifespan)


class EventMessage(BaseModel):
    severity: str
    message: str


class EventMessages(RootModel):
    root: List[EventMessage]


queue = []


@app.post("/send_data")
async def send_data(request: EventMessages):
    logger.info("START")
    for item in request.root:
        data = item.model_dump()
        dt_now = datetime.datetime.now()
        message = (
            data["message"] + " Now DateTime : " + dt_now.strftime("%Y-%m-%d %H:%M:%S")
        )

        id = str(uuid.uuid1())
        data["message"] = message
        data["id"] = id
        global queue
        queue.append(data)

    return {"result": "OK"}


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    logger.info("WebSocket Connection!!!")
    try:
        while True:
            global queue
            try:
                while True:
                    logger.info(f"Status = {websocket.application_state}")
                    logger.info("Current Queue Size = " + str(len(queue)))
                    item = queue.pop(0)
                    await manager.broadcast(item)
                    logger.info(f"send {item}")
            except IndexError:
                logger.info("Waitting !!!")
                await asyncio.sleep(10)
                continue

    except WebSocketDisconnect:
        manager.disconnect(websocket)
