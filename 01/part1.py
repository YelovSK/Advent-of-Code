with open("01\\input.txt") as f:
    lines = f.read().split("\n")[:-1]
    print(sum(int(lines[i-1]) < int(lines[i]) for i in range(len(lines))))