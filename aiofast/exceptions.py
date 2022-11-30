
class ExtractionTypeError(ValueError):
    pass


class UnexpectedContentTypeError(ValueError):
    pass


class MissingContentTypeError(ValueError):
    pass


class UnexpectedHttpCodeError(TypeError):
    pass


class HandlerResultTypeError(TypeError):
    pass


class NotOriginalResponseError(Exception):
    pass


class UnhandledResponseTypeError(TypeError):
    pass


class CannotSerializeResponseError(TypeError):
    pass


class WrongAnnotatedWebResponseError(TypeError):
    pass
