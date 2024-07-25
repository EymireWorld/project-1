from fastapi import APIRouter, Query, status

from app.dependencies import session_dep
from app.schemas import ItemAddSchema, ItemSchema

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
    return await services.get_items(session, limit, offset)


@router.get('/{item_id}')
async def get_item(
    session: session_dep,
    task_id: int
) -> ItemSchema:
    return await services.get_item(session, task_id)


@router.post('', status_code=status.HTTP_201_CREATED)
async def add_item(
    session: session_dep,
    data: ItemAddSchema
) -> ItemSchema:
    return await services.add_item(session, data)
