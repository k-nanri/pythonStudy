from sqlalchemy.ext.asyncio import AsyncSession
from todo import TodoData, Todo


class TodoRepository:

    def __init__(self, session: AsyncSession):
        self.session: AsyncSession = session

    def insert_data(self, todo: TodoData):
        self.session.add(Todo(id=todo.id, content=todo.content))
