import pytest

from riscv_py_emu.dram.controller import DramController
from riscv_py_emu.dram.memory import Dram


@pytest.fixture()
def dram_memory() -> bytes:
    return Dram.MEMORY


@pytest.fixture()
def dram_controller(dram_memory: bytes) -> DramController:
    yield DramController(dram_memory=dram_memory)


def test_creating_dram_controller(dram_controller: DramController) -> None:
    assert dram_controller, "DRAM controller cannot be initialized."
