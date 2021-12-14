from collections import defaultdict

with open("14\\input.txt") as f:
	lines = [line.strip() for line in f.readlines()]
start = [x for x in lines[0]]
pairs = dict(line.split(" -> ")  for line in lines[2:])

pair_count = defaultdict(int)
occurence_map = defaultdict(int)
for x in start:
	occurence_map[x] += 1
for i in range(len(start)-1):
	if start[i] + start[i+1] in pairs:
		pair_count[start[i]+start[i+1]] += 1

for _ in range(40):
	for pair, count in pair_count.copy().items():
		new_char = pairs[pair]	# AC -> B
		occurence_map[new_char] += count	# add B
		pair_count[pair] -= count	# AC -> ABC, AC pair is gone
		pair_count[pair[0] + new_char] += count	# AB from ABC
		pair_count[new_char + pair[1]] += count	# BC from ABC

print(max(occurence_map.values()) - min(occurence_map.values()))