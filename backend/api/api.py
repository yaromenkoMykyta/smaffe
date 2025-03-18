from fastapi import APIRouter
from backend.api.actions.actions_manager import actions_router

api_router = APIRouter(prefix="/api")

api_router.include_router(actions_router)
