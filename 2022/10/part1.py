def check():
    global result

    if (cycle + 20) % 40 == 0:
        result += x * cycle

with open("10/input.txt") as f:
    data = [l.strip() for l in f.readlines()]

x = 1
cycle = 1
result = 0

for line in data:
    cycle += 1
    check()

    if line != "noop":
        x += int(line.split()[1])
        cycle += 1
        check()

print("Part 1:", result)
