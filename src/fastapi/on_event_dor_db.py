from fastapi import FastAPI
from logging import getLogger
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import create_async_engine

from fastapi.responses import JSONResponse

logger = getLogger("uvicorn.app")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Start up!!!")
    url = "postgresql+asyncpg://postgres:example@localhost:5432/postgres"
    engine = create_async_engine(url, echo=True)

    yield

    logger.info("Shutdown!!!")
    engine.dispose()


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
