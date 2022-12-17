from riscv_py_emu.dram.controller import DramController
from riscv_py_emu.dram.memory import OperationSize


class BusController:
    """Class that handles accessing memory via BUS."""

    def __init__(self, dram_controller: DramController) -> None:
        self._dram_controller = dram_controller

    def load(self, address: int, *, size: OperationSize) -> int:
        """Load data of given size from memory."""
        return self._dram_controller.load(address, size=size)

    def store(self, address: int, *, size: OperationSize, value: int) -> None:
        """Store value of given size in memory."""
        return self._dram_controller.store(address, size=size, value=value)

    @property
    def dram_controller(self) -> DramController:
        """Return DRAM controller associated with given BUS."""
        return self._dram_controller
