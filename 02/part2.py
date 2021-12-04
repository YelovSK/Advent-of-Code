with open("02\input.txt") as f:
    horizontal = 0
    depth = 0
    aim = 0
    for line in f:
        dir, val = line.strip().split()
        val = int(val)
        if dir == "forward":
            horizontal += val
            depth += aim * val
        elif dir == "down":
            aim += val
        elif dir == "up":
            aim -= val
    print(horizontal, depth)
    print(horizontal * depth)