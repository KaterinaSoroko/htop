from info.CPU_info import Cpu
from info.memory_info import Memory
from info.process_info import Processes


def main():
    cpu_info = Cpu()
    cpu_info.get()
    cpu_info.show()

    memory_info = Memory()
    memory_info.get()
    memory_info.show()

    process_info = Processes()
    process_info.get()
    process_info.show()


if __name__ == "__main__":
    main()
