from collections import defaultdict

with open("12\\input.txt") as f:
    graph = defaultdict(list)
    for line in f:
        start, end = line.strip().split("-")
        graph[start].append(end)
        graph[end].append(start)

def find_paths(curr, end, visited):
    global res
    if curr == end:
        res += 1
        return

    if curr.islower():
        visited.append(curr)

    for cave in graph[curr]:
        if cave != "start" and len(visited+[cave]) - len(set(visited)) <= 2:
            find_paths(cave, end, visited)

    if curr.islower():
        visited.remove(curr)

res = 0
find_paths("start", "end", list())
print(res)