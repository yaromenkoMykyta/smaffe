from fastapi import APIRouter

import backend.api.actions.actions_service as actions_service


actions_router = APIRouter(prefix="/actions", tags=["actions"])


@actions_router.post("/make_espresso", status_code=200)
def make_espresso():
    actions_service.make_espresso()


@actions_router.post("/make_cream_caffe", status_code=200)
def make_espresso():
    actions_service.make_cream_caffe()
