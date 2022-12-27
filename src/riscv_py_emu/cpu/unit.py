from riscv_py_emu.bus.controller import BusController
from riscv_py_emu.cpu.register import Register
from riscv_py_emu.dram.memory import OperationSize
from riscv_py_emu.instruction.bits_parser import BitsParser
from riscv_py_emu.instruction.opcode import Opcode
from riscv_py_emu.instruction.rv32i_operations import exec_opp_imm
from riscv_py_emu.instruction.rv32i_parsers import imm_j, imm_u, rd
from riscv_py_emu.instruction.rv32i_ui_operations import auipc, lui


class Cpu:
    def __init__(
        self,
        register: Register,
        bus_controller: BusController,
        program_counter: int = 0,
    ) -> None:
        self._program_counter = program_counter
        self._bus_controller = bus_controller
        self._register = register

    def init(self) -> None:
        """Restore CPU to the initial state."""
        self._program_counter = self._bus_controller.dram_controller.dram.base
        self.registry.clean_registers(clear_value=0)
        self.registry[2] = (
            self._bus_controller.dram_controller.dram.base
            + self._bus_controller.dram_controller.dram.size
        )

    def fetch(self) -> int:
        """Return instruction stored under program counter."""
        return self._bus_controller.load(
            self._program_counter, size=OperationSize.UNIT_32
        )

    def exec(self) -> int:
        while instruction := self.fetch():
            print(f"Instruction: {instruction:0x}")
            operation = Opcode(BitsParser(offset=0, size=7).parse(instruction))
            print(operation.name, operation.value)
            match operation:  # noqa: E999
                case Opcode.JAL:
                    rd_val = rd(instruction)
                    imm_j_val = imm_j(instruction)
                    print(f"RD: {rd_val}")
                    print(f"Immediate: {imm_j_val}")
                    self._program_counter += imm_j_val
                case Opcode.OP_IMM:
                    exec_opp_imm(instruction, registry=self.registry)
                    self._program_counter += 4
                case Opcode.LUI:
                    lui(instruction, registry=self.registry)
                    self._program_counter += 4
                case Opcode.AUIPC:
                    auipc(instruction, pc=self.pc, registry=self.registry)
                    self._program_counter += 4
                case _:
                    raise NotImplementedError(operation.name)
                    self._program_counter += 4
        raise Exception("Not implemented yet.")

    def loop(self) -> None:
        while self.pc != 0:
            self.exec()

    @property
    def pc(self) -> int:
        """Return program counter value."""
        return self._program_counter

    @property
    def registry(self) -> Register:
        """Return registry state."""
        return self._register

    @property
    def bus_controller(self) -> BusController:
        """Return BUS controller."""
        return self._bus_controller
