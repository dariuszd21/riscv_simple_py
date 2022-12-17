import pytest

from riscv_py_emu.bus.controller import BusController
from riscv_py_emu.cpu.register import Register
from riscv_py_emu.cpu.unit import Cpu
from riscv_py_emu.dram.controller import DramController
from riscv_py_emu.dram.memory import Dram, OperationSize


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


def test_cpu_init(cpu: Cpu, dram_memory: Dram) -> None:
    cpu.init()
    assert cpu.pc == dram_memory.base, "Init should restore pc to beginning of memory."
    assert cpu.registry[0] == 0, "First registry entry is hardwired to 0."
    assert (
        cpu.registry[2] == dram_memory.base + dram_memory.size
    ), "Stack pointer should point to the top of memory."


def test_cpu_fetch(cpu: Cpu, dram_memory: Dram, bus_controller: BusController) -> None:
    cpu.init()
    example_instruction = 2**10
    bus_controller.store(
        dram_memory.base, size=OperationSize.UNIT_32, value=example_instruction
    )
    example_instruction_fetched = cpu.fetch()
    assert (
        example_instruction_fetched == example_instruction
    ), "CPU cannot correctly read instruction from beginning of the memory."
