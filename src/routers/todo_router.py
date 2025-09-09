from fastapi import APIRouter

from src.config.logger import logger
from src.models.todo import TodoRequest
from src.services.todos import service_add_new_todo, service_get_all_todos

todo_router = APIRouter(prefix="/todos", tags=["todos"])


@todo_router.get("/")
async def get_all_todos():
    todos = await service_get_all_todos()

    return todos


@todo_router.get("/{id}")
async def get_todo_by_id(id: int):
    logger.info("Get todo by ID")
    return "Get todo by ID"


@todo_router.post("/", response_model=TodoRequest)
async def add_new_todo(todo: TodoRequest):
    await service_add_new_todo(todo)

    return todo
