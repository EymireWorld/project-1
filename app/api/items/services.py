from fastapi import HTTPException, status
from sqlalchemy import delete, insert, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import ItemModel
from app.schemas import ItemAddSchema, ItemUpdateSchema


async def get_items(
    session: AsyncSession,
    limit: int,
    offset: int,
) -> list[ItemModel]:
    stmt = select(ItemModel) \
           .offset(offset) \
           .limit(limit)
    result = await session.execute(stmt)

    return result.scalars().all()


async def get_item(
    session: AsyncSession,
    item_id: int
) -> ItemModel:
    stmt = select(ItemModel) \
           .where(ItemModel.id == item_id)
    result = await session.execute(stmt)
    result = result.scalar()

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Item not found.'
        )

    return result


async def add_item(
    session: AsyncSession,
    data: ItemAddSchema
) -> ItemModel:
    stmt = insert(ItemModel) \
           .values(data.model_dump()) \
           .returning(ItemModel)
    result = await session.execute(stmt)
    await session.commit()

    return result.scalar()


async def update_item(
    session: AsyncSession,
    item_id: int,
    data: ItemUpdateSchema
) -> ItemModel:
    stmt = select(ItemModel) \
           .where(ItemModel.id == item_id)
    result = await session.execute(stmt)
    result = result.scalar()

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Item not found.'
        )

    stmt = update(ItemModel) \
           .where(ItemModel.id == item_id) \
           .values(data.model_dump(exclude_unset=True)) \
           .returning(ItemModel)
    result = await session.execute(stmt)
    result = result.scalar()
    await session.execute()

    return result


async def delete_item(
    session: AsyncSession,
    item_id: int
) -> ItemModel:
    stmt = select(ItemModel) \
           .where(ItemModel.id == item_id)
    result = await session.execute(stmt)
    result = result.scalar()

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Item not found.'
        )

    stmt = delete(ItemModel) \
           .where(ItemModel.id == item_id) \
           .returning(ItemModel)
    result = await session.execute(stmt)
    result = result.scalar()
    await session.execute()

    return result
