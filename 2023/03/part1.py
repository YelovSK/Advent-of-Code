import re
from attr import dataclass


with open("2023/03/input.txt") as f:
    lines = f.read().strip().splitlines()

@dataclass(frozen=True)
class LineNumber:
    number: int
    x: int
    y_start: int
    y_end: int

    def __hash__(self) -> int:
        return hash((self.x, self.y_start))


def get_line_numbers(x: int) -> list[LineNumber]:
    res = []

    for match in re.finditer("\d+", lines[x]):
        number = int(match.group())
        res.append(LineNumber(number, x, match.start(), match.end() - 1))

    return res

def get_adjacent(y: int, lines: list[list[LineNumber]]) -> list[LineNumber]:
    res = []

    for line in lines:
        for number in line:
            if number.y_start - 1 <= y <= number.y_end + 1:
                res.append(number)

    return res

line_numbers = [get_line_numbers(x) for x in range(len(lines))]
nums: set[LineNumber] = set()

for x, line in enumerate(lines):
    for y, char in enumerate(line):
        if char.isdigit() or char == ".":
            continue

        # Check x-1, x, x+1
        adjacent = get_adjacent(y, line_numbers[x-1:x+2])
        for adj in adjacent:
            nums.add(adj)

print("Part 2", sum([x.number for x in nums]))