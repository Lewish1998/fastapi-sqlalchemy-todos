from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost/todos"

# Async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Session maker for async sessions
async_session = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

# Base class for ORM models
Base = declarative_base()
