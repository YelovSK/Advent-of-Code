from attr import dataclass
import re

with open("2023/04/input.txt") as f:
    lines = f.read().strip().splitlines()

@dataclass
class Card:
    count: int
    numbers: list[int]

cards: list[Card] = []

# Parse
for i, line in enumerate(lines):
    card, nums = line.split(": ")
    winning_nums, my_nums = nums.split(" | ")

    winning_nums = {int(num) for num in re.findall("\d+", winning_nums)}
    my_nums = {int(num) for num in re.findall("\d+", my_nums)}

    intersection = winning_nums & my_nums
    numbers = [i + j + 1 for j in range(len(intersection))]

    cards.append(Card(1, numbers))

# Add
for number, card in enumerate(cards):
    for number in card.numbers:
        cards[number].count += card.count

print("Part 2", sum([card.count for card in cards]))