class InvalidOperatorSize(Exception):
    """Raised when read/write is done on non-handled size."""


class MemoryOutOfRange(Exception):
    """Raised when read/write is done outside of memory bounds."""
