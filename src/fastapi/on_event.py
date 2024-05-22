from fastapi import FastAPI
from logging import getLogger
from contextlib import asynccontextmanager

logger = getLogger("uvicorn.app")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Start up!!!")
    yield
    logger.info("Shutdown!!!")


app = FastAPI(lifespan=lifespan)


@app.get("/hoge")
async def get_data():
    return {"result": "OK"}


# uvicorn on_event:app --port 8001 --reload
