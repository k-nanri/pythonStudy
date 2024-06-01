from fastapi import FastAPI, WebSocket
from logging import getLogger

logger = getLogger("uvicorn.app")

app = FastAPI()


@app.websocket("/data")
async def websocket_data(websocket: WebSocket):
    logger.info("Begin to accept")
    await websocket.accept()
    logger.info("complite to accept")
    try:
        while True:
            response = await websocket.receive_text()
            logger.info(f"receive {response}")
            await websocket.send_text(f"Message text was {response}")
            logger.info("send message")
    except WebSocketDisconnect:
        
