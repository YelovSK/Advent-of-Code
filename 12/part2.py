from collections import defaultdict

with open("12\\input.txt") as f:
    graph = defaultdict(list)
    for line in f:
        start, end = line.strip().split("-")
        graph[start].append(end)
        graph[end].append(start)

def find_paths(curr, end, path, visited):
    global paths
    if curr == end:
        paths.append(list(path))
        return

    if curr.islower():
        visited.append(curr)
    path.append(curr)

    for cave in graph[curr]:
        if cave != "start" and len(visited+[cave]) - len(set(visited)) <= 2:
            find_paths(cave, end, path, visited)

    path.pop()
    if curr.islower():
        visited.remove(curr)

paths = []
find_paths("start", "end", list(), list())
print(len(paths))