import re

with open("2023/04/input.txt") as f:
    lines = f.read().strip().splitlines()

result = 0

for line in  lines:
    card, nums = line.split(": ")
    winning_nums, my_nums = nums.split(" | ")

    winning_nums = {int(num) for num in re.findall("\d+", winning_nums)}
    my_nums = {int(num) for num in re.findall("\d+", my_nums)}

    intersection = winning_nums & my_nums
    if intersection:
        result += 2 ** (len(intersection) - 1)

print("Part 1", result)