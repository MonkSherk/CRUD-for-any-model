from sqlalchemy import select, join
from sqlalchemy.ext.asyncio import AsyncSession

from views import CRUDBase
from .models import User, ToDo

class CRUDUser(CRUDBase):
    def __init__(self):
        super().__init__(User)

    async def get_todos_for_user(self, user_id: int, db: AsyncSession):
        query = select(ToDo).join(User).where(ToDo.user_id == user_id)
        result = await db.execute(query)
        return result.scalars().all()
