from pathlib import Path
from sys import argv

from riscv_py_emu.bus.controller import BusController
from riscv_py_emu.cpu.register import Register
from riscv_py_emu.cpu.unit import Cpu
from riscv_py_emu.dram.controller import DramController
from riscv_py_emu.dram.memory import Dram


def main() -> None:
    assert len(argv) == 2
    binary_path = Path(argv[1])
    assert binary_path.is_file(), "Provided path is file"
    instructions = binary_path.read_bytes()

    dram_memory = Dram()
    dram_memory.memory[0 : len(instructions)] = instructions
    dram_controller = DramController(dram_memory=dram_memory)
    bus_controller = BusController(dram_controller=dram_controller)
    register = Register()
    cpu = Cpu(bus_controller=bus_controller, register=register)
    cpu.init()
    cpu.loop()


if __name__ == "__main__":
    main()
