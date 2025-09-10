from fastapi import APIRouter, status

from src.models.todo import TodoRequest
from src.services.todos import (
    service_add_new_todo,
    service_get_all_todos,
    service_get_todo_by_id,
)

todo_router = APIRouter(prefix="/todos", tags=["todos"])


@todo_router.get("/")
async def get_all_todos():
    return await service_get_all_todos()


@todo_router.get("/{id}")
async def get_todo_by_id(id: int):
    return await service_get_todo_by_id(id)


@todo_router.post("/", status_code=status.HTTP_201_CREATED, response_model=TodoRequest)
async def add_new_todo(todo: TodoRequest):
    return await service_add_new_todo(todo)
