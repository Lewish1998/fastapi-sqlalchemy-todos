import asyncio

from src.db.db_conn import Base, engine
from src.models.todo import Todo  # noqa: F401


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


asyncio.run(init_db())
