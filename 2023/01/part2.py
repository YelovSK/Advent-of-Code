with open("2023/01/input.txt", "r") as f:
    data = f.read().strip()

num_map = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

result = []

for line in data.splitlines():
    for key, value in num_map.items():
        line = line.replace(key, value)

    nums = [num for num in line if "0" <= num <= "9"]
    result.append(int(nums[0] + nums[-1]))

print("Part 2", sum(result))