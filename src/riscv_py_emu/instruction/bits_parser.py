from functools import lru_cache

from riscv_py_emu.dram.memory import OperationSize
from riscv_py_emu.instruction.exception import (
    IncorrectSizeException,
    InvalidOffsetException,
)


@lru_cache
def max_value(size: int) -> int:
    return 2**size - 1


class BitsParser:
    def __init__(
        self,
        *,
        offset: int,
        size: int,
        instruction_size: OperationSize = OperationSize.UNIT_32,
    ) -> None:
        if size <= 0 or size > instruction_size.bit_size:
            raise IncorrectSizeException(f"Size incorrect ({size})")

        if offset < 0 or offset + size > instruction_size.bit_size:
            raise InvalidOffsetException(
                f"Cannot read instruction at offset {offset} with size {size}"
            )

        self._instruction_size = instruction_size
        self._offset = offset
        self._size = size

    def parse(self, value: int) -> int:
        return (value >> self.offset) & max_value(self._size)

    @property
    def offset(self) -> int:
        return self._offset

    @property
    def size(self) -> int:
        return self._size
