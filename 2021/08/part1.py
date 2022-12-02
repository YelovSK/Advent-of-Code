with open("08\\input.txt") as f:
    outputs = [line.split(" | ")[1].split() for line in f]

res = 0
for line in outputs:
    for o in line:
        if len(o) in (2, 4, 3, 7):
            res += 1

print(res)