from itertools import permutations

with open("08\\input.txt") as f:
    content = f.readlines()

inputs = [line.split(" | ")[0].split() for line in content]
outputs = [line.split(" | ")[1].split() for line in content]

nums = {    # instead of indices like in part2_perm.py there are chars
    "0": "abcefg",
    "1": "cf",
    "2": "acdeg",
    "3": "acdfg",
    "4": "bcdf",
    "5": "abdfg",
    "6": "abdefg",
    "7": "acf",
    "8": "abcdefg",
    "9": "abcdfg"
}

res = 0
for input_line, output_line in zip(inputs, outputs):
    input_line = {"".join(sorted(x)) for x in input_line}
    output_line = ["".join(sorted(x)) for x in output_line]
    for perm in permutations("abcdefg"):
        curr_nums = {"".join(sorted(perm["abcdefg".index(char)] for char in chars)): num for num, chars in nums.items()}
        if input_line == curr_nums.keys():
            res += int("".join([curr_nums[x] for x in output_line]))

print(res)