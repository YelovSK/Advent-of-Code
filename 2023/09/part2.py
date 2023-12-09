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

    rows[-1].appendleft(0)

    for lower_line, upper_line in pairwise(reversed(rows)):
        upper_line.appendleft(upper_line[0] - lower_line[0])

    result += rows[0][0]


print("Part 2", result)