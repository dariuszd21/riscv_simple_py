from riscv_py_emu.instruction.bits_parser import BitsParser


def rd(value: int) -> int:
    """Address of destination register."""
    return BitsParser(offset=7, size=4).parse(value)


def rs1(value: int) -> int:
    """Address of first source register."""
    return BitsParser(offset=15, size=4).parse(value)


def rs2(value: int) -> int:
    """Address of second source register."""
    return BitsParser(offset=20, size=4).parse(value)


def funct3(value: int) -> int:
    """Type of operation selector."""
    return BitsParser(offset=12, size=3).parse(value)


def funct7(value: int) -> int:
    """Additional type of operation selector."""
    return BitsParser(offset=25, size=7).parse(value)


def imm_i(value: int) -> int:
    return BitsParser(offset=20, size=12).parse(value)


def imm_s(value: int) -> int:
    return (BitsParser(offset=25, size=6).parse(value) << 5) | BitsParser(
        offset=7, size=4
    ).parse(value)


def imm_u(value: int) -> int:
    return BitsParser(offset=12, size=20).parse(value) << 12


def imm_b(value: int) -> int:
    return (
        (BitsParser(offset=31, size=1).parse(value) << 12)
        | (BitsParser(offset=7, size=1).parse(value) << 11)
        | (BitsParser(offset=25, size=5).parse(value) << 5)
        | (BitsParser(offset=8, size=4).parse(value) << 1)
    )


def imm_j(value: int) -> int:
    return (
        (BitsParser(offset=31, size=1).parse(value) << 20)
        | (BitsParser(offset=12, size=8).parse(value) << 12)
        | (BitsParser(offset=20, size=1).parse(value) << 11)
        | (BitsParser(offset=21, size=10).parse(value) << 1)
    )
