from app.domain.common.schemas import APIModel
from app.domain.common import enums


class SimpleApiError(APIModel):
    code: enums.ErrorCodes
    message: str
