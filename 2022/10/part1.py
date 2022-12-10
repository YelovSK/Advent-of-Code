from dataclasses import dataclass


@dataclass
class Instruction:
    cycles: int
    add: int


def get_instruction() -> Instruction:
    instruction_str = data.pop()
    if instruction_str == "noop":
        return Instruction(1, 0)
    else:
        number = int(instruction_str.split()[1])
        return Instruction(2, number)


with open("10/input.txt") as f:
    data = [l.strip() for l in f.readlines()][::-1]

instruction = get_instruction()
x = 1
cycle = 1
result = 0

while len(data):
    instruction.cycles -= 1
    if instruction.cycles == 0:
        x += instruction.add
        instruction = get_instruction()

    cycle += 1

    if (cycle + 20) % 40 == 0:
        result += x * cycle

print("Part 1:", result)
