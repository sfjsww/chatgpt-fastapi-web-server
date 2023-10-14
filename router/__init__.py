from fastapi import APIRouter

from .v1 import v1

api_router = APIRouter()

api_router.include_router(
    v1,
    prefix="/v1",
    tags=["v1"],
)
