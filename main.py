from fastapi import FastAPI

from src.routers.todo_router import todo_router

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "Todo App", "docs": "/docs", "version": "0.1.0"}


@app.get("/health")
def health_check():
    return {"status": "OK"}


app.include_router(todo_router)
