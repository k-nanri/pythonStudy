import asyncio
from sqlalchemy import Column
from sqlalchemy import MetaData
from sqlalchemy import select
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.ext.asyncio import create_async_engine

meta = MetaData()
t1 = Table("t1", meta, Column("name", String(50), primary_key=True))


async def async_main() -> None:
    url = "postgresql+asyncpg://postgres:example@localhost:5432/postgres"
    engine = create_async_engine(url, echo=True)

    async with engine.begin() as conn:
        await conn.run_sync(meta.drop_all)
        await conn.run_sync(meta.create_all)

        await conn.execute(
            t1.insert(), [{"name": "some name 1"}, {"name": "some name 2"}]
        )

    async with engine.connect() as conn:
        result = await conn.execute(select(t1).where(t1.c.name == "some name 1"))
        print(result.fetchall())

    await engine.dispose()


asyncio.run(async_main())
