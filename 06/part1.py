with open("06\\input.txt") as f:
    numbers = [int(x) for x in f.read().split(",")]

for _ in range(80):
    add_count = 0
    for i, number in enumerate(numbers):
        if not number:
            numbers[i] = 6
            add_count += 1
        else:
            numbers[i] -= 1
    for _ in range(add_count):
        numbers.append(8)    

print(len(numbers))