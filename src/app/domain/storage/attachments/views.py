from fastapi import APIRouter, Depends, UploadFile
from dependency_injector import wiring
from uuid import UUID

from a8t_tools.db import pagination, sorting

from app.domain.storage.attachments.queries import (
    AttachmentListQuery,
    AttachmentRetrieveQuery,
)
from app.domain.storage.attachments.commands import AttachmentCreateCommand
from app.domain.storage.attachments import schemas
from app.containers import Container
from app.api import deps

router = APIRouter()


@router.post("/create", response_model=schemas.AttachmentAnswer)
@wiring.inject
async def create_attachment(
        attachment: UploadFile,
        command: AttachmentCreateCommand = Depends(wiring.Provide[Container.attachment.create_command]),
) -> schemas.Attachment:
    return await command(
        schemas.AttachmentCreate(
            file=attachment.file,
            name=attachment.filename,
        )
    )


@router.get(
    "/get/list",
    response_model=pagination.CountPaginationResults[schemas.Attachment],
)
@wiring.inject
async def get_attachments_list(
        query: AttachmentListQuery = Depends(wiring.Provide[Container.attachment.list_query]),
        pagination: pagination.PaginationCallable[schemas.Attachment] = Depends(
            deps.get_skip_limit_pagination_dep(schemas.Attachment)
        ),
        sorting: sorting.SortingData[schemas.AttachmentSorts] = Depends(
            deps.get_sort_order_sorting_dep(schemas.AttachmentSorts)
        ),
) -> pagination.Paginated[schemas.Attachment]:
    return await query(schemas.AttachmentListRequestSchema(pagination=pagination, sorting=sorting))


@router.get(
    "/get/{attachment_id}",
    response_model=schemas.Attachment,
)
@wiring.inject
async def get_attachment_details(
        attachment_id: UUID,
        query: AttachmentRetrieveQuery = Depends(wiring.Provide[Container.attachment.retrieve_query]),
) -> schemas.Attachment:
    return await query(attachment_id)
