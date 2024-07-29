from fastapi import APIRouter, Query

from app.dependencies import session_dep
from app.schemas import ItemAddSchema, ItemSchema, ItemUpdateSchema

from . import services


router = APIRouter(
    prefix='/items',
    tags=['Items']
)


@router.get('')
async def get_items(
    session: session_dep,
    limit: int = Query(10, ge=5, le=100),
    offset: int = Query(0, ge=0),
) -> list[ItemSchema]:
    return await services.get_items(session, limit, offset)  # type: ignore


@router.get('/{item_id}')
async def get_item(
    session: session_dep,
    task_id: int
) -> ItemSchema:
    return await services.get_item(session, task_id)


@router.post('')
async def add_item(
    session: session_dep,
    data: ItemAddSchema
) -> ItemSchema:
    return await services.add_item(session, data)


@router.put('/{item_id}')
async def update_item(
    session: session_dep,
    item_id: int,
    data: ItemUpdateSchema
) -> ItemSchema:
    return await services.update_item(session, item_id, data)


@router.delete('/{item_id}')
async def delete_item(
    session: session_dep,
    task_id: int
) -> ItemSchema:
    return await services.delete_item(session, task_id)
