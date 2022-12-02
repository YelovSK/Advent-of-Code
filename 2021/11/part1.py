with open("11\\input.txt") as f:
    octopuses = [[int(x) for x in line.strip()] for line in f]

def flash(i, j):
    global flashed
    if (i, j) in flashed:
        return
    flashed.add((i, j))
    for x in range(i-1, i+1+1):
        for y in range(j-1, j+1+1):
            if x in range(len(octopuses)) and y in range(len(octopuses[0])):
                octopuses[x][y] += 1
                if octopuses[x][y] > 9:
                    flash(x, y)

steps = 100
flash_count = 0
for _ in range(steps):
    flashed = set()
    to_flash = set()
    for i in range(len(octopuses)):
        for j in range(len(octopuses[i])):
            octopuses[i][j] += 1
            if octopuses[i][j] > 9:
                flash(i, j)
    for i, j in flashed:
        octopuses[i][j] = 0
    flash_count += len(flashed)

print("Result:", flash_count)