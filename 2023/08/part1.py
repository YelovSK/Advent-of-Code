with open("2023/08/input.txt") as f:
    lines = f.read().splitlines()

directions = lines[0]

map = dict()

for line in lines[2:]:
    l, r = line.split(" = ")
    a, b, = r[1:-1].split(", ")
    map[l] = (a, b)

current = "AAA"
ix = 0
while current != "ZZZ":
    direction = directions[ix % len(directions)]
    current = map[current][direction == "R"]
    ix += 1

print("Part 1", ix)