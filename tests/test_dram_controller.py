import pytest

from riscv_py_emu.dram._dram_controller import DramController


@pytest.fixture()
def dram_memory() -> bytes:
    return b'0'*1024*1024

@pytest.fixture()
def dram_controller(dram_memory: bytes) -> DramController:
    yield DramController(dram_memory=dram_memory)

def test_creating_dram_controller(dram_controller: DramController) -> None:
    assert dram_controller, 'DRAM controller cannot be initialized.'
