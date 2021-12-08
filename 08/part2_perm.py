from itertools import permutations

with open("08\\input.txt") as f:
    content = f.readlines()

inputs = [line.split(" | ")[0].split() for line in content]
outputs = [line.split(" | ")[1].split() for line in content]

nums = {
    "0": [0, 1, 2, 4, 5, 6],
    "1": [2, 5],
    "2": [0, 2, 3, 4, 6],
    "3": [0, 2, 3, 5, 6],
    "4": [1, 2, 3, 5],
    "5": [0, 1, 3, 5, 6],
    "6": [0, 1, 3, 4, 5, 6],
    "7": [0, 2, 5],
    "8": [0, 1, 2, 3, 4, 5, 6],
    "9": [0, 1, 2, 3, 5, 6]
}

res = 0
for input_line, output_line in zip(inputs, outputs):
    input_line = {"".join(sorted(x)) for x in input_line}
    output_line = ["".join(sorted(x)) for x in output_line]
    for perm in permutations("abcdefg"):
        curr_nums = {"".join(sorted([perm[ix] for ix in index_list])): key for key, index_list in nums.items()}
        if input_line == curr_nums.keys():
            res += int("".join([curr_nums[x] for x in output_line]))

print(res)