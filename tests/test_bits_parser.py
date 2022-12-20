import pytest

from riscv_py_emu.instruction.bits_parser import BitsParser
from riscv_py_emu.instruction.exception import (
    IncorrectSizeException,
    InvalidOffsetException,
)


def test_parsing_correct() -> None:
    value = 0b11010000
    # read [6:4]
    assert BitsParser(offset=4, size=2).parse(value) == 1
    # read [2:0]
    assert BitsParser(offset=0, size=2).parse(value) == 0
    # read [8:6]
    assert BitsParser(offset=6, size=2).parse(value) == 3


def test_wrongly_initialized_parser() -> None:
    with pytest.raises(InvalidOffsetException):
        BitsParser(offset=-2, size=1)


def test_wrong_size() -> None:
    with pytest.raises(IncorrectSizeException):
        BitsParser(offset=0, size=0)
