from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker
from db.todo import TodoData, Todo
from db import database


class TodoRepository:

    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    async def insert_data(self):
        async with self.session() as session:
            async with session.begin():
                session.add_all([Todo(content="test")])

        async with self.session() as session:
            async with session.begin():
                session.add_all([Todo(content="hoge")])


def create_todo_repository() -> TodoRepository:
    engine = database.get_engine()
    async_session = async_sessionmaker(engine, expire_on_commit=True)
    todorepository = TodoRepository(async_session)

    return todorepository
