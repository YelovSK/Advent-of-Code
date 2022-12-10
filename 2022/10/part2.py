def print_pixel():
    global cycle

    if cycle != 0 and cycle % 40 == 0:
        cycle = 0
        print("")
        print_pixel()
    elif cycle - 1 <= x <= cycle + 1:
        print("#", end="")
    else:
        print(".", end="")

with open("10/input.txt") as f:
    data = [l.strip() for l in f.readlines()]

x = 1
cycle = 0
print_pixel()

for line in data:
    cycle += 1
    print_pixel()

    if line != "noop":
        x += int(line.split()[1])
        cycle += 1
        print_pixel()
