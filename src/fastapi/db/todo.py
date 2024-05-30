from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from pydantic import BaseModel, RootModel, ConfigDict


class Base(AsyncAttrs, DeclarativeBase):
    pass


class TodoRequestContent(BaseModel):
    content: str

    class Config:
        orm_mode = True


class TodoRequest(RootModel):
    root: list[TodoRequestContent]

    class Config:
        orm_mode = True


class Todo(Base):
    __tablename__ = "todo"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    content: Mapped[str]


class TodoData(BaseModel):
    id: int
    content: str

    class Config:
        from_attributes = True


class TodoData(RootModel):

    root: list[TodoData]

    class Config:
        from_attributes = True
