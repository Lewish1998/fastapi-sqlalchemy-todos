from src.db.db_conn import async_session
from src.models.todo import Todo, TodoRequest


async def service_add_new_todo(todo: TodoRequest) -> Todo:
    async with async_session() as sesh:
        new_todo = Todo(title=todo.title)
        sesh.add(new_todo)
        await sesh.commit()
        await sesh.refresh(new_todo)
        return new_todo
