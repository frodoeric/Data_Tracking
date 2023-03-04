from swagger_server.models.error_type_enum import ErrorTypeEnum  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501

class BaseCustomError(Exception):
    """Base class for other exceptions"""
    http_code: int
    code: str
    error_type: ErrorTypeEnum
    message: str
    details: str

    def __init__(self, http_code=500, code=None, error_type=None, message=None, details=None):
        self.http_code = http_code
        self.code = code
        self.error_type = error_type
        self.message = message
        self.details = details

    def to_error_response(self):
        return ErrorResponse(code=self.code, type=self.error_type, message=self.message, details=self.details)


class EntityNotFound(BaseCustomError):
    """Raised when the Entity is not found on Database"""
    def __init__(self, http_code=404, code=None, error_type=ErrorTypeEnum.PERSISTENCE, message=None, details=None):
        super().__init__(http_code=http_code, code=code, error_type=error_type,
                         message=message, details=details)


class InvalidPayload(BaseCustomError):
    """Raised when the Request sent has a invalid payload"""
    def __init__(self, http_code=400, code=None, error_type=ErrorTypeEnum.COMMUNICATION, message=None, details=None):
        super().__init__(http_code=http_code, code=code, error_type=error_type,
                         message=message, details=details)

