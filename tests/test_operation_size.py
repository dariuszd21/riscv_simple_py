import pytest

from riscv_py_emu.dram.memory import OperationSize


@pytest.mark.parametrize(
    "operation_size, expected_bit_size",
    (
        (OperationSize.UINT_8, 8),
        (OperationSize.UINT_16, 16),
        (OperationSize.UNIT_32, 32),
        (OperationSize.UINT_64, 64),
    ),
)
def test_operation_size(operation_size: OperationSize, expected_bit_size: int) -> None:
    assert operation_size.bit_size == expected_bit_size, (
        f"Incorrect bit_size returned for: {operation_size}."
        f" Expected {expected_bit_size} != Actual {operation_size.bit_size}"
    )
