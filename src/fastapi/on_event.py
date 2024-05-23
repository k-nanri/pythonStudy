from fastapi import FastAPI
from logging import getLogger
from contextlib import asynccontextmanager
import yaml
from fastapi.responses import JSONResponse

logger = getLogger("uvicorn.app")
messages = []
cnt = 0


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Start up!!!")
    with open("config.yaml", "r") as yml:
        config = yaml.safe_load(yml)
        for item in config["errorlist"]:
            messages.append(item)

    logger.info(messages[0]["status"])
    yield
    logger.info("Shutdown!!!")


app = FastAPI(lifespan=lifespan)


@app.get("/hoge")
async def get_data():
    global cnt
    logger.info(messages)
    if cnt == 0:
        cnt += 1
        return JSONResponse(
            status_code=messages[0]["status"],
            content={"result": messages[0]["message"]},
        )

    if cnt == 1:
        cnt += 1
        return JSONResponse(
            status_code=messages[1]["status"],
            content={"result": messages[1]["message"]},
        )

    if cnt == 2:
        cnt = 0
        return JSONResponse(
            status_code=messages[2]["status"],
            content={"result": messages[2]["message"]},
        )


# uvicorn on_event:app --port 8001 --reload
