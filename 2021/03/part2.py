with open("03\\input.txt") as f:
    lines = [line.strip() for line in f]

def most_common_at_pos(pos):
    ones = 0
    zeroes = 0
    for line in lines:
        if line[pos] == "0":
            zeroes += 1
        elif line[pos] == "1":
            ones += 1
    if ones > zeroes:
        return "1"
    return "0"

gamma = "".join(most_common_at_pos(i) for i in range(len(lines[0])))
epsilon = "".join(["1" if bit == "0" else "0" for bit in gamma])
print("gamma", gamma)   # 802
print("epsilon", epsilon)   # 3293
print("result", 802 * 3293)