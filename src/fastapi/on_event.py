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
        for item in config["errormessages"]:
            messages.append(item)

    logger.info("messages = " + str(messages))
    yield

    logger.info("Shutdown!!!")


app = FastAPI(lifespan=lifespan)


@app.get("/message")
async def get_data():
    global cnt
    logger.info("cnt = " + str(cnt))
    if cnt == 0:
        idx = cnt
        cnt += 1
    elif cnt == 1:
        idx = cnt
        cnt += 1
    elif cnt == 2:
        idx = cnt
        cnt = 0

    response = JSONResponse(
        status_code=messages[idx]["status"],
        content={"result": messages[idx]["message"]},
    )

    logger.info(
        "statuscode = {}, body = {}".format(response.status_code, response.body)
    )
    return response


# uvicorn on_event:app --port 8001 --reload
