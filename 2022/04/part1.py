from attr import dataclass


@dataclass
class Pair:
    first: set[int]
    second: set[int]

    def is_full_overlap(self) -> bool:
        intersection = set(self.first) & set(self.second)
        return len(intersection) == len(self.first) or len(intersection) == len(self.second)

    def is_overlap(self) -> bool:
        return any(set(self.first) & set(self.second))


with open("04/input.txt") as f:
    data = [l.strip().split(",") for l in f.readlines()]

pairs: list[Pair] = []
for l, r in data:
    left_first, left_second = map(int, l.split("-"))
    right_first, right_second = map(int, r.split("-"))

    first_set = set(range(left_first, left_second + 1))
    second_set = set(range(right_first, right_second + 1))

    pairs.append(Pair(first_set, second_set))

full_overlap_count = sum([p.is_full_overlap() for p in pairs])
print("Part 1:", full_overlap_count)
