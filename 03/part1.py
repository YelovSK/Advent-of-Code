with open("03\\input.txt") as f:
    lines = [line.strip() for line in f]

def most_common_at_pos(lines, pos, common=True):
    ones = 0
    zeroes = 0
    for line in lines:
        if line[pos] == "0":
            zeroes += 1
        elif line[pos] == "1":
            ones += 1
    if common and zeroes > ones or not common and ones >= zeroes:
        return "0"
    return "1"

def keep_lines_with(lines, bit, pos):
    return [line for line in lines if line[pos] == bit]

for most_common in True, False:
    pos = 0
    lines_cpy = list(lines)
    while True:
        keep_bit = most_common_at_pos(lines_cpy, pos, most_common)
        lines_cpy = keep_lines_with(lines_cpy, keep_bit, pos)
        if len(lines_cpy) <= 1:
            break
        pos += 1
    if most_common:
        print("O2:", lines_cpy[0])
    else:
        print("CO2:", lines_cpy[0])