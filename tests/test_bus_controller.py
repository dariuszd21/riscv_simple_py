import pytest

from riscv_py_emu.bus.controller import BusController
from riscv_py_emu.dram.controller import DramController
from riscv_py_emu.dram.exception import InvalidOperatorSize, MemoryOutOfRange
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


def test_creating_bus_controller(bus_controller: BusController) -> None:
    assert bus_controller, "BUS controller cannot be initialized."


def test_loading_16_bytes_via_bus(
    dram_memory: Dram, bus_controller: BusController
) -> None:
    addr = dram_memory.base + 4 * (OperationSize.UINT_64.value)
    val = bus_controller.load(addr, size=OperationSize.UINT_16)
    assert val == 0, "There is no data in fake "


def test_loading_18_bytes_raises_exception(
    dram_memory: Dram, bus_controller: BusController
) -> None:
    addr = dram_memory.base + 4 * (OperationSize.UINT_64.value)
    with pytest.raises(InvalidOperatorSize):
        bus_controller.load(addr, size=18)


def test_loading_outside_of_memory(bus_controller: BusController) -> None:
    addr = 4 * (OperationSize.UINT_64.value)
    with pytest.raises(MemoryOutOfRange):
        bus_controller.load(addr, size=OperationSize.UINT_8)


def test_loading_outside_of_memory_upper_range(
    dram_memory: Dram, bus_controller: BusController
) -> None:
    addr = dram_memory.base + dram_memory.size
    with pytest.raises(MemoryOutOfRange):
        bus_controller.load(addr, size=OperationSize.UINT_8)


def test_store_and_load_16_bytes(
    dram_memory: Dram, bus_controller: BusController
) -> None:
    addr = dram_memory.base + 4 * (OperationSize.UINT_64.value)
    value = 1642
    value_size = OperationSize.UINT_16
    bus_controller.store(addr, size=value_size, value=value)
    value_restored = bus_controller.load(addr, size=value_size)
    assert value_restored == value, (
        f"Different value was stored than loaded. "
        f"Stored {value} != Loaded {value_restored}"
    )
