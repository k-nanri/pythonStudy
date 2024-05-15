from fastapi import BackgroundTasks, FastAPI
import time
from logging import getLogger, StreamHandler

app = FastAPI()

logger = getLogger(__name__)
logger.addHandler(StreamHandler())
logger.setLevel("INFO")


def execute_long_time(mode: str, message=""):
    logger.info("--- START execute_log_time")
    logger.info("--- params mode    = " + mode)
    logger.info("--- params message = " + message)
    time.sleep(60)
    logger.info("--- END execute_log_time")


@app.post("/send-notification/{mode}")
async def send_notification(mode: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(execute_long_time, mode, message="notification")
    return {"message": "Notification sent in the background"}


# 起動
# uvicorn backgroundtask:app --reload
