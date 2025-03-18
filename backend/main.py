import uvicorn
from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware

from backend.api.api import api_router
from configs.config import load_config


def run_api():
    app = FastAPI()
    api_config = load_config().api
    app_router = APIRouter()
    app_router.include_router(api_router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=api_config.cors_allowed_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(app_router)
    print(f"Included routes: {app.routes}")

    uvicorn.run(app, host=api_config.host, port=api_config.port)


run_api()
