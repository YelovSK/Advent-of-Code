with open("03/input.txt") as f:
    data = [l.strip() for l in f.readlines()]


def get_priority(char: str) -> int:
    if "a" <= char <= "z":
        return ord(char) - ord("a") + 1
    if "A" <= char <= "Z":
        return ord(char) - ord("A") + 27


triples = [(set(data[i]), set(data[i + 1]), set(data[i + 2])) for i in range(0, len(data), 3)]
result = sum([get_priority((a & b & c).pop()) for a, b, c in triples])

print("Part 2:", result)
