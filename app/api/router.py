from fastapi import APIRouter

from app.api.items.router import router as items_router


router = APIRouter(
    prefix='/api'
)
router.include_router(items_router)
