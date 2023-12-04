from collections import defaultdict

with open("2023/04/input.txt") as f:
    lines = f.read().splitlines()

cards = defaultdict(int)

# Parse
for i, line in enumerate(lines):
    card, nums = line.split(":")
    winning_nums, my_nums = nums.split("|")

    winning_nums = set(winning_nums.split())
    my_nums = set(my_nums.split())

    cards[i] += 1
    for j in range(len(winning_nums & my_nums)):
        cards[i + j + 1] += cards[i]

print("Part 2", sum(cards.values()))