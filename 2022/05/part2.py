with open("05/input.txt") as f:
    crates_data, moves_data = f.read().split("\n\n")

# Imagine parsing the input
crates = {
    1: "BWN",
    2: "LZSPTDMB",
    3: "QHZWR",
    4: "WDVJZR",
    5: "SHMB",
    6: "LGNJHVPB",
    7: "JQZFHDLS",
    8: "WSFJGQB",
    9: "ZWMSCDJ"
}

for key, value in crates.items():
    crates[key] = list(value)

for line in [l.strip() for l in moves_data.split("\n")]:
    _, count, _, where, _, to = line.split(" ")

    moved = []
    for _ in range(int(count)):
        crate = crates[int(where)].pop()
        moved.append(crate)

    crates[int(to)].extend(moved[::-1])

result = "".join(value[-1] for value in crates.values())
print("Part 2:", result)