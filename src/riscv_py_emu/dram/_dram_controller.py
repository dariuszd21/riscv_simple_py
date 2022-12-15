class DramController:
    """Class used to control loading and storing data in fake DDR memory."""

    def __init__(self, *, dram_memory: bytes) -> None:
        self._dram_memory = dram_memory

    @property
    def dram_memory(self) -> bytes:
        """Return internal memory object."""
        return self._dram_memory
