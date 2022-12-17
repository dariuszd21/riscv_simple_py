import pytest

from riscv_py_emu.dram.controller import DramController
from riscv_py_emu.dram.exception import InvalidOperatorSize
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
    addr = Dram.BASE
    with pytest.raises(InvalidOperatorSize):
        dram_controller.load(addr, size=18)
