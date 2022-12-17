import pytest

from riscv_py_emu.bus.controller import BusController
from riscv_py_emu.cpu.register import Register
from riscv_py_emu.cpu.unit import Cpu
from riscv_py_emu.dram.controller import DramController
from riscv_py_emu.dram.memory import Dram


@pytest.fixture()
def dram_memory() -> Dram:
    return Dram()


@pytest.fixture()
def dram_controller(dram_memory: Dram) -> DramController:
    yield DramController(dram_memory=dram_memory)


@pytest.fixture()
def bus_controller(dram_controller: DramController) -> BusController:
    yield BusController(dram_controller=dram_controller)


@pytest.fixture()
def register() -> Register:
    yield Register()


@pytest.fixture()
def cpu(bus_controller: BusController, register: Register) -> Cpu:
    yield Cpu(bus_controller=bus_controller, register=register)


def test_creating_cpu(cpu: Cpu) -> None:
    assert Cpu is not None, "Cpu object cannot be created."

def test_cpu_init(cpu: Cpu) -> None:
    cpu.init()
