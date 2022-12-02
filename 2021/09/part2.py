height_map = []
with open("09\\input.txt") as f:
    for line in f:
        height_map.append([int(i) for i in line.strip()])

x_size, y_size = len(height_map), len(height_map[0])
basins = []

def basin_rec(i, j):
    if height_map[i][j] == 9:
        return
    basins[-1].add((i, j))
    for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
        if x in range(x_size) and y in range(y_size):
            if height_map[x][y] > height_map[i][j]:
                basin_rec(x, y)

for i, row in enumerate(height_map):
    for j, point in enumerate(row):
        check_pts = [point]
        for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
            if x in range(x_size) and y in range(y_size):
                check_pts.append(height_map[x][y])
        if min(check_pts) == point and check_pts.count(min(check_pts)) == 1:
            basins.append(set())
            basin_rec(i, j)

basins = sorted(basins, key=len)[::-1]
print(len(basins[0]) * len(basins[1]) * len(basins[2]))