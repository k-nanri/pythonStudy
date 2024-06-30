from fastapi import FastAPI
from logging import getLogger

logger = getLogger("uvicorn.app")

app = FastAPI()


@app.get("/item")
async def get_items():

    logger.info("Receive GET Request.")

    return {"status": "OK"}


@app.post("/item")
async def post_item(body: dict):

    logger.info("Receive POST Request.")
    logger.info(f"body : {body}")

    return {"status": "OK"}
