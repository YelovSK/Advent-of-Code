# this is disgusting, I don't wanna see this ever again

with open("08\\input.txt") as f:
    content = f.readlines()

outputs = [line.split(" | ")[1].split() for line in content]
inputs = [line.split(" | ")[0].split() for line in content]

def get_segments(input_map):
    segments = [set() for _ in range(7)]
    # 1, 7 -> guaranteed position 0
    chars = "".join(input_map[2]) + "".join(input_map[3])
    for i in chars:
        if chars.count(i) == 1:
            segments[0] = i
    segments[5] |= set(input_map[2][0])
    segments[2] |= set(input_map[2][0])
    
    # 4, 2
    chars4 = input_map[4][0]
    chars1 = input_map[2][0]
    chars = chars4+chars1
    for i in chars:
        if chars.count(i) == 1:
            segments[1].add(i)
            segments[3].add(i)

    # 2, 3, 5 -> guaranteed position 3, 4, 1
    chars = "".join(input_map[5])
    for char in chars:
        if chars.count(char) == 1:
            if char in segments[1]:
                segments[1] = char
                segments[3] = "".join(segments[3]-set(char))
            elif char not in segments[3]:
                segments[4] = char
    
    # 0, 6, 9 -> guaranteed position 2, 5
    chars = "".join(input_map[6])
    for char in chars:
        if chars.count(char) == 2:  # bud 3 (middle), 2 (upper right), 4 (down left)
            if char not in segments[3] and char not in segments[4]:
                segments[2] = char
                segments[5] = "".join(set(segments[5])-set(char))

    all_chars = {"a", "b", "c", "d", "e", "f", "g"}
    curr_chars = set()
    for seg in segments:
        for char in seg:
            curr_chars.add(char)
    segments[6] = "".join(all_chars - curr_chars)   # guaranteed position 6
    return segments

def get_segment_nums(segments):
    nums = {i:"" for i in range(10)}
    for i in (0, 1, 2, 4, 5, 6):
        nums[0] += segments[i]
    for i in (2, 5):
        nums[1] += segments[i]
    for i in (0, 2, 3, 4, 6):
        nums[2] += segments[i]
    for i in (0, 2, 3, 5, 6):
        nums[3] += segments[i]
    for i in (1, 2, 3, 5):
        nums[4] += segments[i]
    for i in (0, 1, 3, 5, 6):
        nums[5] += segments[i]
    for i in (0, 1, 3, 4, 5, 6):
        nums[6] += segments[i]
    for i in (0, 2, 5):
        nums[7] += segments[i]
    for i in range(7):
        nums[8] += segments[i]
    for i in (0, 1, 2, 3, 5, 6):
        nums[9] += segments[i]
    return nums

def find_segment_num(nums, output):
    res = ""
    for num in output:
        for key, val in nums.items():
            if sorted(val) == sorted(num):
                res += str(key)
    return int(res)

sum_res = 0
for input_line, output_line in zip(inputs, outputs):
    input_map = {}
    for i in input_line:
        if len(i) not in input_map:
            input_map[len(i)] = [i]
        else:
            input_map[len(i)].append(i)
    segments = get_segments(input_map)
    nums = get_segment_nums(segments)
    res = find_segment_num(nums, output_line)
    sum_res += res

print(sum_res)