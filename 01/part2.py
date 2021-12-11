with open("01\\input.txt") as f:
    lines = [int(x) for x in [line.strip() for line in f]]

print(sum(sum(lines[i:i+3]) < sum(lines[i+1:i+4]) for i in range(len(lines)-3)))