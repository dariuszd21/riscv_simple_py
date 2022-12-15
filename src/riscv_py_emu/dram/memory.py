class Dram:
    BASE = 0x80000000  # Offset in which actual memory is accessible
    SIZE = 1024 * 1024  # 1Mb
    MEMORY = b"0" * SIZE
