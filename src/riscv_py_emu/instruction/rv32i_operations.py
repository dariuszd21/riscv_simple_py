from enum import IntEnum

from riscv_py_emu.cpu.register import Register
from riscv_py_emu.instruction.rv32i_parsers import funct3, funct7, imm_i, rd, rs1


class OpImmFunc3(IntEnum):
    ADDI = 0b000
    SLTI = 0b010
    SLTIU = 0b011
    XORI = 0b100
    ORI = 0b110
    ANDI = 0b111
    SLLI = 0b001
    SRI = 0b101


class OpImmFunc7(IntEnum):
    SRLI = 0b0000000
    SRAI = 0b0100000


def exec_opp_imm(instruction: int, *, registry: Register) -> None:
    """Execute immediate integer operation"""
    f3 = OpImmFunc3(funct3(instruction))
    print(f"Executing f3: {f3.name}")
    match f3:
        case OpImmFunc3.ADDI:
            addi(instruction, registry=registry)
        case OpImmFunc3.SLTI:
            slti(instruction, registry=registry)
        case OpImmFunc3.SLTIU:
            sltiu(instruction, registry=registry)
        case OpImmFunc3.ORI:
            ori(instruction, registry=registry)
        case OpImmFunc3.ANDI:
            andi(instruction, registry=registry)
        case OpImmFunc3.SLLI:
            slli(instruction, registry=registry)
        case OpImmFunc3.SRI:
            f7 = OpImmFunc7(funct7(instruction))
            print(f"Executing f7: {f7.name}")
            match f7:
                case OpImmFunc7.SRLI:
                    srli(instruction, registry=registry)
                case OpImmFunc7.SRAI:
                    srai(instruction, registry=registry)


def addi(instruction: int, *, registry: Register) -> None:
    """Add immediate to source registry value."""
    destination_registry = rd(instruction)
    source_reg = rs1(instruction)
    registry[destination_registry] = registry[source_reg] + imm_i(instruction)


def slti(instruction: int, *, registry: Register) -> None:
    """Set rd to 1 if source register is less than immediate (sign-extended)."""
    destination_registry = rd(instruction)
    source_reg = rs1(instruction)
    registry[destination_registry] = (
        1 if registry[source_reg] < imm_i(instruction) else 0
    )


def sltiu(instruction: int, *, registry: Register) -> None:
    """Set rd to 1 if source register is less than immediate (unsigned-extended)."""
    destination_registry = rd(instruction)
    source_reg = rs1(instruction)
    registry[destination_registry] = (
        1 if registry[source_reg] < imm_i(instruction) else 0
    )


def andi(instruction: int, *, registry: Register) -> None:
    """Logical AND between immediate and rs1 (sign-extended)."""
    destination_registry = rd(instruction)
    source_reg = rs1(instruction)
    registry[destination_registry] = registry[source_reg] & imm_i(instruction)


def ori(instruction: int, *, registry: Register) -> None:
    """Logical OR between immediate and rs1 (sign-extended)."""
    destination_registry = rd(instruction)
    source_reg = rs1(instruction)
    registry[destination_registry] = registry[source_reg] | imm_i(instruction)


def xori(instruction: int, *, registry: Register) -> None:
    """Logical XOR between immediate and rs1 (sign-extended)."""
    destination_registry = rd(instruction)
    source_reg = rs1(instruction)
    registry[destination_registry] = registry[source_reg] ^ imm_i(instruction)


def slli(instruction: int, *, registry: Register) -> None:
    """Perform logical left shift."""


def srli(instruction: int, *, registry: Register) -> None:
    """Perform logical right shift."""


def srai(instruction: int, *, registry: Register) -> None:
    """Perform arithmetical right shift."""
