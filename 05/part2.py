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
    # I feel sicc from this spaghett
    # I lost all of my 2 remaining brain cells trying to do diagonal because I guess Python doesn't have inclusive range
    y1, x1, y2, x2 = line
    if x1 == x2:
        if y1 > y2:
            y1, y2 = y2, y1
        for y_coord in range(y1, y2+1):
            diagram[x1][y_coord] += 1
    elif y1 == y2:
        if x1 > x2:
            x1, x2 = x2, x1
        for x_coord in range(x1, x2+1):
            diagram[x_coord][y1] += 1
    elif abs(x2-x1) == abs(y2-y1):
        x_incl = -1 if x2 < x1 else 1
        y_incl = -1 if y2 < y1 else 1
        for _ in range(abs(x2 - x1) + 1):
            diagram[x1][y1] += 1
            x1 += x_incl
            y1 += y_incl

count = 0
for row in diagram:
    for col in row:
        if col > 1:
            count += 1
print(count)