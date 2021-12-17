f = open("17\\input.txt").read().strip()[13:]
x_coords, y_coords = f.split(", ")
x1, x2 = x_coords[2:].split("..")
y1, y2 = y_coords[2:].split("..")

def i_range(start, end):
    if end < start:
        return range(start, end-1, -1)
    return range(start, end+1)

xrange = i_range(int(x1), int(x2))
yrange = i_range(int(y1), int(y2))
max_x = max(xrange)
min_y = min(yrange)

def shoot(dx, dy):
    x, y = 0, 0
    while x < max_x and y > min_y:
        x += dx
        y += dy
        if x in xrange and y in yrange:
            return True
        if dx > 0:
            dx -= 1
        dy -= 1
    return False

count = 0
for dx in range(max_x+1):
    for dy in range(min_y, 500):
        if shoot(dx, dy):
            count += 1
print(count)