with open("2023/02/input.txt") as f:
    data = f.read().strip()

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

result = 0

for line in data.splitlines():
    game, sets = line.split(": ")
    game_id = int(game.split(" ")[1])

    valid = True

    max_r, max_g, max_b = 0, 0, 0

    for set in sets.split("; "):
        r, g, b = 0, 0, 0
        cubes = set.split(", ")

        for cube in cubes:
            count, color = cube.split(" ")
            count = int(count)
            if color == "red":
                r += count
            elif color == "green":
                g += count
            elif color == "blue":
                b += count

        max_r = max(max_r, r)
        max_g = max(max_g, g)
        max_b = max(max_b, b)

    result += max_r * max_g * max_b

print("Part 2", result)