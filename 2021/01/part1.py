with open("01\\input.txt") as f:
    lines = [line.strip() for line in f]

print(sum(int(lines[i-1]) < int(lines[i]) for i in range(len(lines))))