import networkx as nx

with open("15\\input.txt") as f:
    arr = [[int(x) for x in line.strip()] for line in f.readlines()]

width, height = len(arr), len(arr[0])
l_width, l_height = width * 5, height * 5

graph = nx.DiGraph()
for x, y in [(x, y) for x in range(l_width) for y in range(l_height)]:
    cost = arr[x % width][y % height] + x // width + y // height
    if cost > 9:
        cost %= 9
    for new_x, new_y in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
        graph.add_edge((new_x, new_y), (x, y), weight=cost)

res = nx.shortest_path_length(graph, (0, 0), (l_width - 1, l_height - 1), weight="weight")
print(res)