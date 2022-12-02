from re import findall as fa

x1, x2, y1, y2 = [int(s) for s in fa("[-\d]+", open("17\\input.txt").read().strip())]
xrange = range(min(x1, x2), max(x1, x2)+1)
yrange = range(min(y1, y2), max(y1, y2)+1)
max_x = max(xrange)
min_y = min(yrange)

def hit_count():    # shit is faster with PyPy if the loop is inside a function

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

    for dx in range(max_x+1):
        for dy in range(min_y, 500):
            yield shoot(dx, dy)

print(sum(hit_count()))