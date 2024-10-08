from fastapi import FastAPI, Depends
from .crud import CRUDUser, CRUDToDo
from .database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI()

crud_user = CRUDUser()
crud_todo = CRUDToDo()

# Создание пользователя
@app.post("/users/")
async def create_user(username: str, email: str, db: AsyncSession = Depends(get_db)):
    return await crud_user.create({"username": username, "email": email}, db)

# Создание задачи
@app.post("/todos/")
async def create_todo(title: str, description: str, user_id: int, db: AsyncSession = Depends(get_db)):
    return await crud_todo.create({"title": title, "description": description, "user_id": user_id}, db)

# Получение задач для пользователя
@app.get("/users/{user_id}/todos/")
async def get_todos_for_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return await crud_user.get_todos_for_user(user_id, db)
