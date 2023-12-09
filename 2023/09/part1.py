from collections import deque
from itertools import pairwise


with open("2023/09/input.txt") as f:
    lines = f.read().splitlines()

result = 0

for line in lines:
    rows: deque[deque[int]] = deque()
    rows.append(deque(map(int, line.split())))

    while any(rows[-1]):
        rows.append(deque(b - a for a, b in pairwise(rows[-1])))

    rows[-1].append(0)

    for lower_line, upper_line in pairwise(reversed(rows)):
        upper_line.append(lower_line[-1] + upper_line[-1])

    result += rows[0][-1]


print("Part 1", result)