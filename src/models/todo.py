from pydantic import BaseModel
from sqlalchemy import Column, Integer, String

from src.db.db_conn import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)


class TodoRequest(BaseModel):
    title: str


class TodoResponse(BaseModel):
    id: int
    title: str
