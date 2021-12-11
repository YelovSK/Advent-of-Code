with open("02\input.txt") as f:
    horizontal = 0
    depth = 0
    for line in f:
        dir, val = line.strip().split()
        val = int(val)
        if dir == "forward":
            horizontal += val
        elif dir == "down":
            depth += val
        elif dir == "up":
            depth -= val
    print(horizontal * depth)