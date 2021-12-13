import numpy as np

with open("13\\input.txt") as f:
    content = f.read()

coords, folding = content.split("\n\n")
folding = [fold for fold in folding.split("\n") if fold]
x_coords = []
y_coords = []
for c in coords.split("\n"):
    x = int(c.split(",")[0])
    y = int(c.split(",")[1])
    x_coords.append(x)
    y_coords.append(y)
x_size = int(folding[0].split("=")[1]) * 2
y_size = int(folding[1].split("=")[1]) * 2
dots = [["." for _ in range(x_size+1)] for _ in range(y_size+1)]
for x, y in zip(x_coords, y_coords):
    dots[y][x] = "#"    # flipped, cuz idk

def fold_list(coord, num):
    if coord == "x":
        axis = 1
        larger = [r[:num] for r in dots]
        smoler = [r[num+1:] for r in dots]
    elif coord == "y":
        axis = 0
        larger = dots[:num]
        smoler = dots[num+1:]
    smoler = np.flip(smoler, axis)
    new_dots = list(larger)
    for i in range(len(smoler)):
        for j in range(len(smoler[i])):
            if smoler[i][j] == "#":
                new_dots[i][j] = "#"
    return new_dots

for fold in folding:
    coord, num = fold.split("=")
    dots = fold_list(coord.split()[2], int(num))

print('\n'.join(map(''.join, dots)))