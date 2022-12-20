from riscv_py_emu.bus.controller import BusController
from riscv_py_emu.cpu.register import Register
from riscv_py_emu.dram.memory import OperationSize
from riscv_py_emu.instruction.bits_parser import BitsParser
from riscv_py_emu.instruction.opcode import Opcode


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
        operation = Opcode(BitsParser(offset=0, size=7).parse(self.fetch()))
        print(operation.name, operation.value)
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
