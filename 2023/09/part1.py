from collections import deque
from itertools import islice


with open("2023/09/input.txt") as f:
    lines = f.read().splitlines()

result = 0

for line in lines:
    rows: deque[deque[int]] = deque()
    rows.append(deque(map(int, line.split())))

    while any(num != 0 for num in rows[-1]):
        rows.append(deque(b - a for a, b in zip(rows[-1], islice(rows[-1], 1, None))))

    rows[-1].append(0)

    for lower_line, upper_line in zip(reversed(rows), islice(reversed(rows), 1, None)):
        upper_line.append(lower_line[-1] + upper_line[-1])

    result += rows[0][-1]


print("Part 1", result)