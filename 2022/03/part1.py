with open("03/input.txt") as f:
    data = [l.strip() for l in f.readlines()]


def get_priority(char: str) -> int:
    if "a" <= char <= "z":
        return ord(char) - ord("a") + 1
    if "A" <= char <= "Z":
        return ord(char) - ord("A") + 27


halves: list[tuple[set, set]] = []
for line in data:
    half_length = len(line) // 2
    first_half = set(line[:half_length])
    second_half = set(line[half_length:])
    halves.append((first_half, second_half))

result = sum([get_priority((l & r).pop()) for l, r in halves])

print("Part 1:", result)
