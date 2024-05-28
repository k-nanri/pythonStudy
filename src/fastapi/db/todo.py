from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from pydantic import BaseModel


class Base(AsyncAttrs, DeclarativeBase):
    pass


class Todo(Base):
    __tablename__ = "todo"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    content: Mapped[str]


class TodoData(BaseModel):
    id: str
    content: str
