with open("06/input.txt") as f:
    data = f.read()

COUNT = 4;
for ix in range(len(data) - COUNT):
    chars = data[ix:ix + COUNT]
    if len(set(chars)) == COUNT:
        print("Part 1:", ix + COUNT)
        break