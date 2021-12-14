from collections import defaultdict
from copy import copy

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

steps = 40
for _ in range(steps):
	new_pair_count = copy(pair_count)
	for pair, count in pair_count.items():
		new_char = pairs[pair]
		occurence_map[new_char] += count
		new_pair_count[pair] -= count	# XX -> XAX, XX pair is gone
		n1, n2 = pair[0] + new_char, new_char + pair[1]	# XYX: XY, YX
		if n1 in pairs:
			new_pair_count[n1] += count
		if n2 in pairs:
			new_pair_count[n2] += count
	pair_count = new_pair_count

print(max(occurence_map.values()) - min(occurence_map.values()))