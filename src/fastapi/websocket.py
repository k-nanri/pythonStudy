import asyncio
import uuid
from logging import getLogger

logger = getLogger("uvicorn.app")

from fastapi import (
    Depends,
    FastAPI,
    WebSocket,
    WebSocketException,
)

app = FastAPI()


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        while True:
            id = str(uuid.uuid1())
            logger.info(f"id = {id}")
            severity = "info"
            message = "Restart Server"
            event = {"id": id, "severity": severity, "message": message}
            await websocket.send_json(event)
            await asyncio.sleep(10)
