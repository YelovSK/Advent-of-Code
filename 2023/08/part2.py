import math

with open("2023/08/input.txt") as f:
    lines = f.read().splitlines()


directions = lines[0]

map = dict()

for line in lines[2:]:
    l, r = line.split(" = ")
    a, b, = r[1:-1].split(", ")
    map[l] = (a, b)

nodes = [node for node in map.keys() if node.endswith("A")]

ix = 0
lcm = []

for node_ix, node in enumerate(nodes):
    ix = 0

    while not nodes[node_ix].endswith("Z"):
        direction = directions[ix % len(directions)]
        nodes[node_ix] = map[nodes[node_ix]][direction == "R"]
        ix += 1

    lcm.append(ix)


print("Part 2", math.lcm(*lcm))