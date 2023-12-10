import sys

with open("2023/10/input.txt") as f:
    data = f.read().strip()


map = dict()

lines = data.splitlines()

ABOVE_CONNECTIONS = ("7", "F", "|", "S")
BELOW_CONNECTIONS = ("L", "J", "|", "S")
LEFT_CONNECTIONS = ("L", "F", "-", "S")
RIGHT_CONNECTIONS = ("7", "J", "-", "S")

def get_connections(x, y):
    c = lines[x][y]
    res = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue

            if i != 0 and j != 0:
                continue

            xx = x + i
            yy = y + j

            if xx < 0 or yy < 0:
                continue

            if xx >= len(lines) or yy >= len(lines[0]):
                continue

            cc = lines[xx][yy]
            if cc == ".":
                continue

            if xx == x - 1 and c in ("|", "L", "J", "S") and cc in ABOVE_CONNECTIONS:
                res.append((xx, yy))
            elif xx == x + 1 and c in ("|", "7", "F", "S") and cc in BELOW_CONNECTIONS:
                res.append((xx, yy))
            elif yy == y - 1 and c in ("-", "7", "J", "S") and cc in LEFT_CONNECTIONS:
                res.append((xx, yy))
            elif yy == y + 1 and c in ("-", "F", "L", "S") and cc in RIGHT_CONNECTIONS:
                res.append((xx, yy))

    return res

start = None

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == ".":
            continue
        map[(i, j)] = get_connections(i, j)
        if char == "S":
            start = (i, j)

for k, v in map.items():
    print(k, v)

# Find longest path from start (cannot visit same node twice)
def dfs(node, visited):
    if node in visited:
        return 0

    visited.add(node)

    res = 1
    for child in map[node]:
        res = max(res, dfs(child, visited) + 1)

    visited.remove(node)

    return res


sys.setrecursionlimit(10**6)
print("Part 1", dfs(start, set()) // 2)
