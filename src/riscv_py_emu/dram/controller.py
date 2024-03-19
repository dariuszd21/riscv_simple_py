from riscv_py_emu.dram.exception import InvalidOperatorSize, MemoryOutOfRange
from riscv_py_emu.dram.memory import Dram, OperationSize


class DramController:
    """Class used to control loading and storing data in fake DDR memory."""

    def __init__(self, *, dram_memory: Dram) -> None:
        self._dram = dram_memory

    @property
    def dram_memory(self) -> bytes:
        """Return internal memory representation."""
        return self._dram.memory

    @property
    def dram(self) -> Dram:
        """Expose DRAM object."""
        return self._dram

    def load(self, address: int, *, size: OperationSize) -> int:
        """Load data of given size from memory."""
        normalized_address = address - self._dram.base
        match size:
            case OperationSize(size):
                self._memory_bounds_check(normalized_address, size)
                return self._load(normalized_address, size=size)
            case _:
                raise InvalidOperatorSize(f"Load of unexpected size: ({size})")

    def store(self, address: int, *, size: OperationSize, value: int) -> None:
        """Store value of given size in memory."""
        normalized_address = address - self._dram.base
        match size:
            case OperationSize(size):
                self._memory_bounds_check(normalized_address, size=size)
                return self._store(normalized_address, size=size, value=value)
            case _:
                raise InvalidOperatorSize(f"Load of unexpected size: ({size})")

    def _load(self, address: int, *, size: OperationSize) -> int:
        """Load memory of given size from memory."""
        return int.from_bytes(
            self.dram_memory[address : address + size.value], byteorder="little"
        )

    def _store(self, address: int, *, size: OperationSize, value: int) -> None:
        """Load memory of given size from memory."""
        self.dram_memory[address : address + size.value] = value.to_bytes(
            length=size.value, byteorder="little"
        )

    def _memory_bounds_check(self, address: int, size: OperationSize) -> None:
        """Check if"""
        if address < 0:
            raise MemoryOutOfRange(
                f"Reading from restricted address: {address}"
                f"Which is outside of range {self._dram.base}..{self._dram.size}"
            )
        dram_slice_len = len(self.dram_memory[address : address + size.value])
        if dram_slice_len != size.value:
            raise MemoryOutOfRange(
                f"Read incorrect number of bytes. Expected read of size: {size.value} "
                f"!= Available memory: {dram_slice_len}"
            )
