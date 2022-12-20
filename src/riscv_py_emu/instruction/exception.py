class InvalidOffsetException(Exception):
    """Exception thrown when incorrect offset is provided."""


class IncorrectSizeException(Exception):
    """Exception thrown when parser read more than maximum instruction size."""
