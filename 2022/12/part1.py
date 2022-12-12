import collections


def bfs(grid: list[list[int]],
        start: tuple[int, int],
        end: tuple[int, int]
        ) -> list[tuple[int, int]]:

    queue = collections.deque([[start]])
    seen = set(start)
    paths = []

    while queue:
        path = queue.popleft()
        x, y = path[-1]
        curr_value = grid[x][y]

        if (x, y) == end:
            paths.append(path)

        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if not (0 <= x2 < ROWS and 0 <= y2 < COLS):
                continue

            next_value = grid[x2][y2]

            if (x2, y2) not in seen and next_value <= curr_value + 1:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
    
    return paths

with open("12/input.txt") as f:
    data = [l.strip() for l in f.readlines()]

ROWS = len(data)
COLS = len(data[0])

grid = [[None] * COLS for _ in range(ROWS)]
for row_ix, line in enumerate(data):
    for col_ix, c in enumerate(line):
        if c == "S":
            c = "a"
            start = (row_ix, col_ix)
        elif c == "E":
            end = (row_ix, col_ix)
            c = "z"
        grid[row_ix][col_ix] = ord(c)

paths = bfs(grid, start, end)
shortest = min(paths, key=lambda x: len(x))
print("Part 2:", len(shortest) - 1)
