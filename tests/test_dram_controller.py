import pytest

from riscv_py_emu.dram.controller import DramController
from riscv_py_emu.dram.exception import InvalidOperatorSize, MemoryOutOfRange
from riscv_py_emu.dram.memory import Dram, OperationSize


@pytest.fixture()
def dram_memory() -> bytes:
    return Dram.MEMORY


@pytest.fixture()
def dram_controller(dram_memory: bytes) -> DramController:
    yield DramController(dram_memory=dram_memory)


def test_creating_dram_controller(dram_controller: DramController) -> None:
    assert dram_controller, "DRAM controller cannot be initialized."


def test_loading_16_bytes(dram_controller: DramController) -> None:
    addr = Dram.BASE + 4 * (OperationSize.UINT_64.value)
    val = dram_controller.load(addr, size=OperationSize.UINT_16)
    assert val == 0, "There is no data in fake "


def test_loading_18_bytes_raises_exception(dram_controller: DramController) -> None:
    addr = Dram.BASE + 4 * (OperationSize.UINT_64.value)
    with pytest.raises(InvalidOperatorSize):
        dram_controller.load(addr, size=18)


def test_loading_outside_of_memory(dram_controller: DramController) -> None:
    addr = 4 * (OperationSize.UINT_64.value)
    with pytest.raises(MemoryOutOfRange):
        dram_controller.load(addr, size=OperationSize.UINT_8)


def test_loading_outside_of_memory_upper_range(dram_controller: DramController) -> None:
    addr = Dram.BASE + Dram.SIZE
    with pytest.raises(MemoryOutOfRange):
        dram_controller.load(addr, size=OperationSize.UINT_8)


def test_store_and_load_16_bytes(dram_controller: DramController) -> None:
    addr = Dram.BASE + 4 * (OperationSize.UINT_64.value)
    value = 1642
    value_size = OperationSize.UINT_16
    dram_controller.store(addr, size=value_size, value=value)
    value_restored = dram_controller.load(addr, size=value_size)
    assert value_restored == value, "Same value was stored and loaded from memory."
