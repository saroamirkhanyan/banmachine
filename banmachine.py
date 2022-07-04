PUSH = "դնել"
POP = "վերցնել"
WRITE = "գրել"
EXIT = "ավարտ"


class BanMachine:
    def __init__(
        self,
        memory,
        instruction_pointer_pointer,
        stack_pointer_pointer
    ):
        self.memory = memory
        self.instruction_pointer_pointer = instruction_pointer_pointer
        self.stack_pointer_pointer = stack_pointer_pointer
        self.exited = False

    def get_instruction_pointer(self):
        return int(self.memory[instruction_pointer_pointer])

    def get_stack_pointer(self):
        return int(self.memory[self.stack_pointer_pointer])

    def set_stack_pointer(self, new_stack_pointer):
        self.memory[self.stack_pointer_pointer] = new_stack_pointer 

    def stack_pop(self):
        stack_pointer = self.get_stack_pointer() 
        self.set_stack_pointer(stack_pointer - 1)
        return self.memory[stack_pointer] 

    def do(self):
        instruction_pointer = self.get_instruction_pointer()
        instruction = self.memory[instruction_pointer]
        stack_pointer = self.get_stack_pointer()
        if instruction == PUSH:
            operand = self.memory[instruction_pointer + 1]
            stack_pointer += 1
            self.set_stack_pointer(stack_pointer)
            self.memory[stack_pointer] = operand
            self.memory[self.instruction_pointer_pointer] += 2
            return
        elif instruction == POP:
            stack_pointer -= 1
            self.set_stack_pointer(stack_pointer)
        elif instruction == WRITE:
            data = int(self.stack_pop())
            address = int(self.stack_pop())
            self.memory[address] = data
        elif instruction == EXIT:
            self.exited = True
        self.memory[self.instruction_pointer_pointer] += 1

program = """
դնել 20
դնել 10
գրել
ավարտ
"""

program_in_memory = sum(
    map(
        lambda line: line.split(" "),
        program.strip().split("\n")
    ),
    []
)

MEMORY_SIZE = 100
STACK_SIZE = 10

memory = program_in_memory + [None] * (MEMORY_SIZE - len(program_in_memory))

instruction_pointer_pointer = 98
memory[instruction_pointer_pointer] = 0

stack_pointer_pointer = 99

memory[stack_pointer_pointer] = len(memory) - STACK_SIZE - 1

banmachine = BanMachine(
    memory,
    instruction_pointer_pointer,
    stack_pointer_pointer
)

while not banmachine.exited:
    banmachine.do()
print(memory)