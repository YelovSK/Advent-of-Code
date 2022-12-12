import collections


def bfs(grid: dict[tuple[int, int], str], start: tuple[int, int], end: tuple[int, int]) -> list[tuple[int, int]]:
    queue = collections.deque([[start]])
    seen = set(start)
    paths = []

    while queue:
        path = queue.popleft()
        x, y = path[-1]
        curr_value = grid[(x, y)]

        if (x, y) == end:
            paths.append(path)

        for x2, y2 in ((x + 1,y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if x2 < 0 or y2 < 0 or x2 >= HEIGHT or y2 >= WIDTH:
                continue

            next_value = grid[(x2, y2)]

            if (x2, y2) not in seen and ord(next_value) <= ord(curr_value) + 1:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
    
    return paths

with open("12/input.txt") as f:
    data = [l.strip() for l in f.readlines()]

HEIGHT = len(data)
WIDTH = len(data[0])

grid_map = {}
for row_ix, line in enumerate(data):
    for col_ix, c in enumerate(line):
        if c == "S":
            c = "a"
            start = (row_ix, col_ix)
        elif c == "E":
            end = (row_ix, col_ix)
            c = "z"
        grid_map[(row_ix, col_ix)] = c

paths = bfs(grid_map, start, end)
shortest = min(paths, key=lambda x: len(x))
print("Part 1:", len(shortest) - 1)
