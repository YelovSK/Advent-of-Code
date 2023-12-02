with open("2023/01/input.txt", "r") as f:
    data = f.read().strip()

result = []

for line in data.splitlines():
    nums = [num for num in line if "0" <= num <= "9"]
    result.append(int(nums[0] + nums[-1]))

print("Part 1", sum(result))    