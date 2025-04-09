"""
This module initializes and runs a FastAPI server.

The `run_api` function sets up the FastAPI application, configures middleware,
includes API routes, and starts the server using Uvicorn. It also loads the
necessary configuration for the API, such as CORS settings, host, and port.
"""

import uvicorn
from fastapi import FastAPI, APIRouter
from starlette.middleware.cors import CORSMiddleware

from backend.api.api import api_router
from configs.config import ConfigLoader


def run_api():
    """
    Initialize the FastAPI server with specified parameters and run the API.

    :return: None
    """
    app = FastAPI()
    api_config = ConfigLoader.load_config().api

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

    uvicorn.run(app, host=api_config.host, port=api_config.port)


if __name__ == "__main__":
    run_api()
