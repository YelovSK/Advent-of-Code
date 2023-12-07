from enum import Enum
from collections import Counter


with open("2023/07/input.txt") as f:
    lines = f.read().splitlines()

cards_values = {c: i for i, c in enumerate("AKQJT98765432"[::-1])}

class HandRank(Enum):
    FIVE_OF_A_KIND = 7
    FOUR_OF_A_KIND = 6
    FULL_HOUSE = 5
    THREE_OF_A_KIND = 4
    TWO_PAIR = 3
    ONE_PAIR = 2
    HIGH_CARD = 1

class Hand:
    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.bid = bid
        self.kind = self._get_kind()

    def _get_kind(self) -> HandRank:
        counts = sorted(Counter(self.cards).values())

        match counts:
            case [5]:
                return HandRank.FIVE_OF_A_KIND
            case [1, 4]:
                return HandRank.FOUR_OF_A_KIND
            case [2, 3]:
                return HandRank.FULL_HOUSE
            case [1, 1, 3]:
                return HandRank.THREE_OF_A_KIND
            case [1, 2, 2]:
                return HandRank.TWO_PAIR
            case [1, 1, 1, 2]:
                return HandRank.ONE_PAIR
            case [1, 1, 1, 1, 1]:
                return HandRank.HIGH_CARD

    def __lt__(self, other: 'Hand') -> bool:
        if self.kind != other.kind:
            return self.kind.value < other.kind.value

        for c1, c2 in zip(self.cards, other.cards):
            if cards_values[c1] != cards_values[c2]:
                return cards_values[c1] < cards_values[c2]

        return False

hands: list[Hand] = []

for line in lines:
    cards, bid = line.split()
    hands.append(Hand(cards, int(bid)))

result = sum((ix + 1) * hand.bid for ix, hand in enumerate(sorted(hands)))

print("Part 1", result)