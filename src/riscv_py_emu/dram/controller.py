from riscv_py_emu.dram.exception import InvalidOperatorSize
from riscv_py_emu.dram.memory import Dram, OperationSize


class DramController:
    """Class used to control loading and storing data in fake DDR memory."""

    def __init__(self, *, dram_memory: bytes) -> None:
        self._dram_memory = dram_memory

    @property
    def dram_memory(self) -> bytes:
        """Return internal memory object."""
        return self._dram_memory

    def load(self, address: int, *, size: OperationSize) -> int:
        normalized_address = address - Dram.BASE
        match size:  # noqa: E999
            case OperationSize(size):
                return self._load(normalized_address, size=size)
            case _:
                raise InvalidOperatorSize(f"Load of unexpected size: ({size})")

    def _load(self, address: int, *, size: OperationSize) -> int:
        """Load memory of given size from memory."""
        return int.from_bytes(
            self._dram_memory[address : address + size.value], byteorder="little"
        )
