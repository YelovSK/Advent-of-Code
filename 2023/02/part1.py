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

        if r > MAX_RED or g > MAX_GREEN or b > MAX_BLUE:
            valid = False
            break

    if valid:
        result += game_id

print("Part 1", result)