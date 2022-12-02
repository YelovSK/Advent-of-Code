def i_range(start, end):
    if end < start:
        return range(start, end-1, -1)
    return range(start, end+1)

lines = []  # [x1, y1, x2, y2]
max_coord = 0

with open("05\\input.txt") as f:
    for line in f:
        left, right = line.split(" -> ")
        coords_left = [int(x) for x in left.strip().split(",")]
        coords_right = [int(x) for x in right.strip().split(",")]
        coords = coords_left + coords_right
        if max(coords) > max_coord:
            max_coord = max(coords) + 2 # why's +1 index out of range?
        lines.append(coords)

diagram = [[0 for _ in range(max_coord)] for _ in range(max_coord)]

for line in lines:
    x1, y1, x2, y2 = line
    if x1 == x2:
        for y_coord in i_range(y1, y2):
            diagram[x1][y_coord] += 1
    elif y1 == y2:
        for x_coord in i_range(x1, x2):
            diagram[x_coord][y1] += 1

count = 0
for row in diagram:
    for col in row:
        if col > 1:
            count += 1
print(count)