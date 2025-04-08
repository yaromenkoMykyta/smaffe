from fastapi import APIRouter

import backend.api.actions.actions_service as actions_service


actions_router = APIRouter(prefix="/actions", tags=["actions"])


@actions_router.post("/make_espresso", status_code=200)
def make_espresso():
    """
    processing of the /make_espresso API request

    it calls the actions service function for the next actions

    :return: None
    """
    actions_service.make_espresso()


@actions_router.post("/make_cream_caffe", status_code=200)
def make_espresso():
    """
    processing of the /make_cream_caffe API request

    it calls the actions service function for the next actions

    :return: None
    """
    actions_service.make_cream_caffe()
