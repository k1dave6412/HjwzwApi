from fastapi import FastAPI
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from backend.core.config import ALLOWED_HOSTS, API_PREFIX, DEBUG, PROJECT_NAME, VERSION
from backend.core.events import create_start_app_handler, create_stop_app_handler
from backend.router import router as api_router


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_event_handler("startup", create_start_app_handler(application))
    application.add_event_handler("shutdown", create_stop_app_handler(application))
    application.include_router(api_router, prefix=API_PREFIX)
    return application


app = get_application()

print("Document Available On http://127.0.0.1:8000/docs")


# NOTE: 架構參考：https://github.com/nsidnev/fastapi-realworld-example-app
