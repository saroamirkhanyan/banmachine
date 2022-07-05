PUSH = "դնել"
POP = "վերցնել"
WRITE = "գրել"
READ = "կարդալ"
EXIT = "ավարտ"
PRINT = "տպել"


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
        self.started = False

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

    def stack_push(self, data):
        stack_pointer = self.get_stack_pointer()
        stack_pointer += 1
        self.set_stack_pointer(stack_pointer)
        self.memory[stack_pointer] = data

    def do(self):
        instruction_pointer = self.get_instruction_pointer()
        instruction = self.memory[instruction_pointer]
        stack_pointer = self.get_stack_pointer()
        if instruction == PUSH:
            operand = self.memory[instruction_pointer + 1]
            self.stack_push(int(operand))
            self.memory[self.instruction_pointer_pointer] += 2
            return
        elif instruction == POP:
            stack_pointer -= 1
            self.set_stack_pointer(stack_pointer)
        elif instruction == WRITE:
            data = self.stack_pop()
            address = self.stack_pop()
            self.memory[address] = data
        elif instruction == READ:
            self.stack_push(self.memory[self.stack_pop()])
        elif instruction == EXIT:
            self.exited = True
        elif instruction == PRINT:
            print(self.stack_pop())
        self.memory[self.instruction_pointer_pointer] += 1

program = """
կարդալ
տպել
ավարտ
"""

program_in_memory = sum(
        map(
            lambda line: line.split(" "),
            program.strip().split("\n")
            ),
        []
        )

MEMORY_SIZE = 30
STACK_SIZE = 10

memory = program_in_memory + [None] * (MEMORY_SIZE - len(program_in_memory))

instruction_pointer_pointer = 28
memory[instruction_pointer_pointer] = 0

stack_pointer_pointer = 29

memory[stack_pointer_pointer] = len(memory) - STACK_SIZE - 4

banmachine = BanMachine(
        memory,
        instruction_pointer_pointer,
        stack_pointer_pointer
        )

while not banmachine.exited:
    banmachine.do()

def print_memory(memory):
    for i in range(len(memory)):
        print(str(i) + ": " + str(memory[i]))
#print_memory(memory)
