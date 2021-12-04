with open("01\\input.txt") as f:
    lines = f.read().strip().split("\n")
    lines = [int(i) for i in lines]
    print(sum(sum(lines[i:i+3]) < sum(lines[i+1:i+4]) for i in range(len(lines)-3)))