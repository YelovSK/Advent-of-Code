import networkx as nx

with open("15\\input.txt") as f:
	arr = [[int(x) for x in line.strip()] for line in f.readlines()]

width, height = len(arr), len(arr[0])

graph = nx.DiGraph()
for x, y in [(x, y) for x in range(width) for y in range(height)]:
	for new_x, new_y in (x-1, y), (x+1, y), (x, y-1), (x, y+1):
		try:
			graph.add_edge((x, y), (new_x, new_y), weight=arr[new_x][new_y])
		except IndexError:
			pass

res = nx.shortest_path_length(graph, (0, 0), (width-1, height-1), weight="weight")
print(res)