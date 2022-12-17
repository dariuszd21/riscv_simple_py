from enum import IntEnum


class Dram:
    BASE = 0x80000000  # Offset in which actual memory is accessible
    SIZE = 1024 * 1024  # 1Mb
    MEMORY = b"\0" * SIZE


class OperationSize(IntEnum):
    UINT_8 = 1
    UINT_16 = 2
    UNIT_32 = 4
    UINT_64 = 8
