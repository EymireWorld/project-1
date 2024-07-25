from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import ItemModel
from app.schemas import ItemAddSchema


async def get_items(
    session: AsyncSession,
    limit: int,
    offset: int,
):
    stmt = select(ItemModel).offset(offset).limit(limit)
    result = await session.execute(stmt)
    result = result.scalars()

    if result != None:
        return list(result.all())
    return None


async def get_item(
    session: AsyncSession,
    item_id: int
):
    stmt = select(ItemModel).where(ItemModel.id == item_id)
    result = await session.execute(stmt)

    return result.scalar()


async def add_item(
    session: AsyncSession,
    data: ItemAddSchema
):
    stmt = insert(ItemModel).values(data.model_dump()).returning(ItemModel)
    result = await session.execute(stmt)
    await session.commit()

    return result.scalar()
