from riscv_py_emu.cpu.register import Register
from riscv_py_emu.instruction.rv32i_parsers import imm_u, rd


def lui(instruction: int, *, registry: Register) -> None:
    """Load upper intermediate into registy."""
    registry[rd(instruction)] = imm_u(instruction)


def auipc(instruction: int, *, pc: int, registry: Register) -> None:
    """Load upper intermediate into registy."""
    registry[rd(instruction)] = pc + imm_u(instruction)
