"""
This module defines the FastAPI router for the API.

It includes the main API router and integrates other routers, such as the
actions router, to handle specific API endpoints.
"""

from fastapi import APIRouter
from backend.api.actions.actions_manager import actions_router

# Create the main API router with a prefix for all API endpoints
api_router = APIRouter(prefix="/api")

# Include the actions router to handle actions-related endpoints
api_router.include_router(actions_router)
