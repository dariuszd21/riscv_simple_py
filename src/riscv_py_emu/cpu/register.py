from collections import UserDict

from riscv_py_emu.cpu.exception import (
    InvalidRegisterKeyType,
    InvalidRegisterKeyValue,
    InvalidRegisterSize,
)


class Register(UserDict):
    def __init__(self, register_size: int = 32) -> None:
        if register_size < 0:
            raise InvalidRegisterSize(
                f"Cannot create register with size: {register_size}"
            )
        self._register_size = register_size
        super().__init__((i, 0) for i in range(register_size))

    def __setitem__(self, key: int, value: int) -> None:
        if not isinstance(key, int):
            raise InvalidRegisterKeyType(
                f"Registry should be integer, not {type(key)}."
            )
        if not (0 <= key < self._register_size):
            raise InvalidRegisterKeyValue(
                f"Registry should be from range 0..{self._register_size}"
                f", actual value {key}."
            )
        super().__setitem__(key, value)

    def clean_registers(self, *, clear_value: int = 0) -> None:
        for k in self.data:
            self.data[k] = clear_value
