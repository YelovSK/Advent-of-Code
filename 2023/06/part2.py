import cmath
import math

with open("2023/06/input.txt") as f:
    lines = f.read().splitlines()

time = int("".join(lines[0].split()[1:]))
distance = int("".join(lines[1].split()[1:]))

# -(run_time**2) + (race_time*run_time) - distance = 0
a, b, c = -1, time, -distance
d = (b ** 2) - (4 * a * c)
max = (-b - cmath.sqrt(d)) / (2 * a)
min = (-b + cmath.sqrt(d)) / (2 * a)
result = math.ceil(max.real - 1) - math.floor(min.real + 1) + 1

print("Part 2", result)