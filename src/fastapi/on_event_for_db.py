from fastapi import FastAPI, Depends
from logging import getLogger
from contextlib import asynccontextmanager
from fastapi.responses import JSONResponse
from db import database
from db.repository import TodoRepository, create_todo_repository
from db.todo import TodoData

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


@app.get("/data")
async def get_data(repository: TodoRepository = Depends(create_todo_repository)):
    response = await repository.get_data()
    logger.info(response)
    return TodoData(response)


# uvicorn on_event:app --port 8001 --reload
