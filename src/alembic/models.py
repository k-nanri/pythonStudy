from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, Integer, String
from settings import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    fullname: Mapped[str] = mapped_column(String)
    nickname: Mapped[str] = mapped_column(String)
    age: Mapped[int] = mapped_column()

    def __repr__(self):
        return "<User('name={}', fullname={}, nickname={})>".format(
            self.name, self.fullname, self.nickname
        )
