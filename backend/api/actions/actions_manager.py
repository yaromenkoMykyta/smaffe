"""
This module defines the FastAPI router for handling actions-related API endpoints.

It includes endpoints for:
- Making an espresso
- Making a cream caffe

Each endpoint delegates the business logic to the
corresponding functions in the `actions_service` module.
"""

from fastapi import APIRouter

from backend.api.actions import actions_service

# Create a router for handling actions-related API endpoints
actions_router = APIRouter(prefix="/actions", tags=["actions"])


@actions_router.post("/make_espresso", status_code=200)
def make_espresso():
    """
    Handle the /make_espresso API request.

    This endpoint triggers the process of making an espresso by calling
    the corresponding function in the actions service.

    :return: None
    """
    actions_service.make_espresso()


@actions_router.post("/make_cream_caffe", status_code=200)
def make_cream_caffe():
    """
    Handle the /make_cream_caffe API request.

    This endpoint triggers the process of making a cream caffe by calling
    the corresponding function in the actions service.

    :return: None
    """
    actions_service.make_cream_caffe()
