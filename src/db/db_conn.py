from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

from src.config.settings import settings

DB_USERNAME = settings.DB_USERNAME.get_secret_value()
DB_PASSWORD = settings.DB_PASSWORD.get_secret_value()


DATABASE_URL = f"postgresql+asyncpg://{DB_USERNAME}:{DB_USERNAME}@localhost/todos"

engine = create_async_engine(DATABASE_URL, echo=True)

async_session = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()
