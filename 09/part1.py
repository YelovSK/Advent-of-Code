height_map = []
with open("09\\input.txt") as f:
    for line in f:
        height_map.append([int(i) for i in line.strip()])

x_size, y_size = len(height_map), len(height_map[0])
low_points = []

for i, row in enumerate(height_map):
    for j, point in enumerate(row):
        check_pts = [point]
        for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
            if x in range(x_size) and y in range(y_size):
                check_pts.append(height_map[x][y])
        if min(check_pts) == point and check_pts.count(min(check_pts)) == 1:
            low_points.append(point)

print(sum(i+1 for i in low_points))