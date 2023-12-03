import re
from attr import dataclass


with open("2023/03/input.txt") as f:
    lines = f.read().strip().splitlines()

@dataclass
class LineNumber:
    number: int
    y_start: int
    y_end: int

def get_line_numbers(x: int) -> list[LineNumber]:
    res = []

    for match in re.finditer("\d+", lines[x]):
        number = int(match.group())
        res.append(LineNumber(number, match.start(), match.end() - 1))

    return res


line_numbers = [get_line_numbers(x) for x in range(len(lines))]
result = 0

for x, line in enumerate(lines):
    for y, char in enumerate(line):
        if char != "*":
            continue

        # Check x-1, x, x+1
        adjacent: list[LineNumber] = []
        for l in line_numbers[x-1:x+2]:
            adjacent.extend([number for number in l if (number.y_start - 1 <= y <= number.y_end + 1)])

        if len(adjacent) == 2:
            result += adjacent[0].number * adjacent[1].number


print("Part 2", result)