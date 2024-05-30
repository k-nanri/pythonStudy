from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from db.todo import Todo, TodoRequest
from db import database
from sqlalchemy import select
from logging import getLogger

logger = getLogger("uvicorn.app")


class TodoRepository:

    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def insert_data(self, request: TodoRequest):
        async with self.session() as session:
            async with session.begin():
                insert_data = []
                for item in request.root:
                    logger.info(item.model_dump_json())
                    insert_data.append(Todo(item.model_dump_json()))

                logger.info(insert_data)
                session.add_all(insert_data)

    async def get_data(self):
        async with self.session() as session:
            stmt = select(Todo)
            result = await session.execute(stmt)
            response = result.scalars().all()
            for data in result.scalars():
                logger.info("id = " + str(data.id) + ", content = " + data.content)
                response.append(response)

        return response


def create_todo_repository() -> TodoRepository:
    engine = database.get_engine()
    async_session = async_sessionmaker(engine, expire_on_commit=True)
    todorepository = TodoRepository(async_session)

    return todorepository
