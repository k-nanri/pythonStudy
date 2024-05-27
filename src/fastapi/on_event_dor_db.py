from fastapi import FastAPI, Depends
from logging import getLogger
from contextlib import asynccontextmanager
from fastapi.responses import JSONResponse
from db import database
from db.repository import TodoRepository, create_todo_repository

logger = getLogger("uvicorn.app")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Start up!!!")
    await database.connect()

    yield
    database.disconnect()
    logger.info("Shutdown!!!")


app = FastAPI(lifespan=lifespan)


@app.post("/data")
async def create_data(repository: TodoRepository = Depends(create_todo_repository)):
    await repository.insert_data()
    await repository.insert_data()


@app.get("/message")
async def get_data(repository: TodoRepository = Depends(create_todo_repository)):
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
