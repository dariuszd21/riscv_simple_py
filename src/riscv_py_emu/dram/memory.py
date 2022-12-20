from dataclasses import dataclass, field
from enum import Enum, IntEnum, auto


@dataclass()
class Dram:
    base: int = 0x80000000  # Offset in which actual memory is accessible
    size: int = 1024 * 1024  # 1MiB
    memory_initializer: int = 0
    memory: bytearray = field(init=False)

    def __post_init__(self) -> None:
        self.memory = bytearray([self.memory_initializer]) * self.size


class OperationSize(IntEnum):
    UINT_8 = 1
    UINT_16 = 2
    UNIT_32 = 4
    UINT_64 = 8

    @property
    def bit_size(self) -> int:
        return 8 * self.value


class MemoryOperation(Enum):
    LOAD = auto()
    STORE = auto()
