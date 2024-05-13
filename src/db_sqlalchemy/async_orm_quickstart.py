from __future__ import annotations
import asyncio
import datetime
from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import selectinload


class Base(AsyncAttrs, DeclarativeBase):
    pass


class B(Base):
    __tablename__ = "b"

    id: Mapped[int] = mapped_column(primary_key=True)
    a_id: Mapped[int] = mapped_column(ForeignKey("a.id"))
    data: Mapped[str]


class A(Base):
    __tablename__ = "a"

    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[str]
    create_date: Mapped[datetime.datetime] = mapped_column(server_default=func.now())
    bs: Mapped[List[B]] = relationship()


async def insert_objects(async_session: async_sessionmaker[AsyncSession]) -> None:
    async with async_session() as session:
        async with session.begin():
            session.add_all(
                [
                    A(
                        bs=[B(data="b1"), B(data="b2")],
                        data="a1",
                        create_date=datetime.datetime.now(),
                    ),
                    A(
                        bs=[],
                        data="as",
                        create_date=datetime.datetime.now(),
                    ),
                    A(
                        bs=[B(data="b3"), B(data="b4")],
                        data="a3",
                        create_date=datetime.datetime.now(),
                    ),
                ]
            )


async def select_and_update_objects(
    async_session: async_sessionmaker[AsyncSession],
) -> None:
    async with async_session() as session:
        stmt = select(A).order_by(A.id).options(selectinload(A.bs))
        result = await session.execute(stmt)

        for a in result.scalars():
            print(a, a.data)
            print(f"created at: {a.create_date}")
            for b in a.bs:
                print(b, b.data)

        result = await session.execute(select(A).order_by(A.id).limit(1))
        a1 = result.scalars().one()
        a1.data = "new data"

        await session.commit()

        print(a1.data)

        for b1 in await a1.awaitable_attrs.bs:
            print(b1, b1.data)


async def async_main() -> None:

    url = "postgresql+asyncpg://postgres:example@localhost:5432/postgres"
    engine = create_async_engine(url, echo=True)
    async_session = async_sessionmaker(engine, expire_on_commit=False)

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    await insert_objects(async_session)
    await select_and_update_objects(async_session)
    await engine.dispose()


asyncio.run(async_main())
