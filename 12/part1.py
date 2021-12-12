from collections import defaultdict

with open("12\\input.txt") as f:
    graph = defaultdict(list)
    for line in f:
        start, end = line.strip().split("-")
        graph[start].append(end)
        graph[end].append(start)

def find_paths(curr, end, visited, curr_path):
    global paths
    if curr == end:
        paths.append(curr_path)
        return

    if curr.islower():
        visited.add(curr)
    curr_path.append(curr)

    for cave in graph[curr]:
        if cave not in visited or cave.isupper():
            find_paths(cave, end, visited, curr_path)
                    
    curr_path.pop()
    if curr.islower():
        visited.remove(curr)

paths = []
find_paths("start", "end", set(), list())

res = 0
for path in paths:
    lower = [cave for cave in path if cave.islower()]
    if len(lower) == len(set(lower)):
        res += 1

print(res)