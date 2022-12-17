class InvalidRegisterSize(Exception):
    """Exception raised if size of register is wrongly defined."""


class InvalidRegisterKeyType(Exception):
    """Registry is overwritten with key of unexpected type."""


class InvalidRegisterKeyValue(Exception):
    """Registry is overwritten on unexpected address."""
