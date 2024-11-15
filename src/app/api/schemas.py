from app.domain.common import enums
from app.domain.common.schemas import APIModel


class SimpleApiError(APIModel):
    code: enums.ErrorCodes
    message: str
