from dataclasses import dataclass


@dataclass
class Pair:
    first: set[int]
    second: set[int]

    def is_full_overlap(self) -> bool:
        return self.first <= self.second or self.second <= self.first

    def is_overlap(self) -> bool:
        return any(set(self.first) & set(self.second))


with open("04/input.txt") as f:
    data = [l.strip().split(",") for l in f.readlines()]

pairs: list[Pair] = []
for l, r in data:
    left_start, left_end = map(int, l.split("-"))
    right_start, right_end = map(int, r.split("-"))

    left_set = set(range(left_start, left_end + 1))
    right_set = set(range(right_start, right_end + 1))

    pairs.append(Pair(left_set, right_set))

overlap_count = sum([p.is_overlap() for p in pairs])
print("Part 2:", overlap_count)
