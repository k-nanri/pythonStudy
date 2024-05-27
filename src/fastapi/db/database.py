from sqlalchemy.ext.asyncio import create_async_engine
from todo import Base

URL = "postgresql+asyncpg://postgres:example@localhost:5432/postgres"
engine = None


async def connect():
    global engine

    # エンジンオブジェクトの生成
    engine = create_async_engine(URL, echo=True)

    # テーブル作成
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


def get_engine():
    return engine


def disconnect():
    engine.dispose()
