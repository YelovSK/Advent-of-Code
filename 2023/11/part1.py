import itertools


with open("2023/11/input.txt") as f:
    lines = f.read().splitlines()

rows = [i for i, line in enumerate(lines) if all(char == "." for char in line)]
columns = [i for i in range(len(lines[0])) if all(line[i] == "." for line in lines)]
galaxies = [(r, c) for r, line in enumerate(lines) for c, char in enumerate(line) if char == "#"]

EXPANSION = 2

result = 0

for (r1, c1), (r2, c2) in itertools.combinations(galaxies, 2):
    distance = abs(r1 - r2) + abs(c1 - c2)
    row_offset = sum(EXPANSION - 1 for row in rows if min(r1, r2) < row < max(r1, r2))
    column_offset = sum(EXPANSION - 1 for column in columns if min(c1, c2) < column < max(c1, c2))
    result += distance + row_offset + column_offset

print("Part 2", result)