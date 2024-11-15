import enum


class ErrorCodes(enum.StrEnum):
    api_error = enum.auto()
    not_found = enum.auto()
    auth_error = enum.auto()
    permission_error = enum.auto()
    database_error = enum.auto()


class TaskNames(enum.StrEnum):
    activate_user = enum.auto()
    reminder_news = enum.auto()


class TaskQueues(enum.StrEnum):
    main_queue = enum.auto()
