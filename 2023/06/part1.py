import math

with open("2023/06/input.txt") as f:
    lines = f.read().splitlines()

times = [int(x) for x in lines[0].split()[1:]]
distances = [int(x) for x in lines[1].split()[1:]]

result = 1

for time, distance in zip(times, distances):
    # -(run_time**2) + (race_time*run_time) - distance = 0
    a, b, c = -1, time, -distance
    d = (b ** 2) - (4 * a * c)
    max = (-b - math.sqrt(d)) / (2 * a)
    min = (-b + math.sqrt(d)) / (2 * a)

    result *= math.ceil(max - 1) - math.floor(min + 1) + 1

print("Part 1", result)