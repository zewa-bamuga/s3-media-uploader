from fastapi import APIRouter, status

import app.domain.storage.attachments.views

from app.api import schemas

storage_router = APIRouter(prefix="/storage")
storage_router.include_router(
    app.domain.storage.attachments.views.router,
    prefix="/v1/attachments",
    tags=["attachments"],
)

router = APIRouter(
    responses={
        status.HTTP_403_FORBIDDEN: {"model": schemas.SimpleApiError},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": schemas.SimpleApiError},
    }
)

router.include_router(storage_router)
