from pydantic import BaseModel
from sqlalchemy import Column, Integer, String

from src.db.db_conn import Base


class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(String, nullable=False)


class TodoRequest(BaseModel):
    title: str
    description: str | None = None
    status: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {"title": "Title", "description": "Description", "status": "Complete"}
            ]
        }
    }


class TodoResponse(BaseModel):
    id: int
    title: str
