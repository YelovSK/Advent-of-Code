with open("01/input.txt", "r") as f:
    data = f.read()

elves = [e.split("\n") for e in data.split("\n\n")]
elves = [[int(n) for n in e if n] for e in elves]

sums = [sum(x) for x in elves]
sums.sort()

print("Part 1", sums[-1])
