from riscv_py_emu.bus.controller import BusController
from riscv_py_emu.cpu.register import Register


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
