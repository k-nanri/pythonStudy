from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import create_engine


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")
    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r}, user=" + str(user) +")"
    
# DBエンジンを作成
url = "postgresql://postgres:example@localhost:5432/postgres"
engine = create_engine(url, echo=True)

# テーブルをDBに作成
Base.metadata.create_all(engine)

# セッションを作成
# セッションを介してクエリを実行する
with Session(engine) as session:
    spongebob = User(
        name="spongebob",
        fullname="Spongebob Squarepants",
        addresses=[Address(email_address="spongebob@sqlalchemy.org")],
    )
    sandy = User(
        name="sandy",
        fullname="Sandy Cheeks",
        addresses=[
            Address(email_address="sandy@sqlalchemy.org"),
            Address(email_address="sandy@squirrelpower.org"),
        ],
    )
    patrick = User(name="patrick", fullname="Patrick Star")
    session.add_all([spongebob, sandy, patrick])
    session.commit()


session = Session(engine)

stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))

print("SELECT")
for user in session.scalars(stmt):
    print(user)

print("SELECT JOIN")
stmt = (
    select(Address)
    .join(Address.user)
    .add_columns(User.name)
    .where(User.name == "sandy")
    .where(Address.email_address == "sandy@sqlalchemy.org")
)
print(stmt)
sandy_address = session.scalars(stmt)
print("SELECT JOIN RESULT")
for result in sandy_address:
    print(result)

"""
結合したデータはリレーションシップで定義した変数の中に設定される
"""