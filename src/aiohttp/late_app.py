from fastapi import FastAPI
import time
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


@app.get("/")
def call_api():
    logger.info("Received request in late app.")
    time.sleep(10)
    response = {"message": "success"}
    return response


# 下記で起動
# uvicorn late_app:app --port 8000
