from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from fastapi import HTTPException, status

class CRUDBase:
    def __init__(self, model):
        self.model = model

    async def create(self, obj_in: dict, db: AsyncSession) -> object:
        db_obj = self.model(**obj_in)
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def get(self, obj_id: int, db: AsyncSession) -> object:
        db_obj = await db.get(self.model, obj_id)
        if not db_obj:
            raise HTTPException(status_code=404, detail="Object not found")
        return db_obj

    async def update(self, obj_id: int, obj_in: dict, db: AsyncSession) -> object:
        db_obj = await self.get(obj_id, db)
        for field, value in obj_in.items():
            setattr(db_obj, field, value)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def delete(self, obj_id: int, db: AsyncSession):
        db_obj = await self.get(obj_id, db)
        await db.delete(db_obj)
        await db.commit()
        return {"message": "Object deleted successfully"}

    async def get_all(self, db: AsyncSession) -> list:
        query = select(self.model)
        result = await db.execute(query)
        return result.scalars().all()
