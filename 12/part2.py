from collections import defaultdict

with open("12\\input.txt") as f:
    graph = defaultdict(list)
    for line in f:
        start, end = line.strip().split("-")
        graph[start].append(end)
        graph[end].append(start)

def find_paths(curr, end, visited, duplicate=None):
    global res
    if curr == end:
        res += 1
        return

    if curr in visited:
        duplicate = curr
    if curr.islower():
        visited.append(curr)

    for cave in graph[curr]:
        if cave != "start" and (cave not in visited or not duplicate):
            find_paths(cave, end, visited, duplicate)

    if curr.islower():
        visited.remove(curr)

res = 0
find_paths("start", "end", list())
print(res)