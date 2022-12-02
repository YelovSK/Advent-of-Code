from collections import Counter

with open("14\\input.txt") as f:
    lines = [line.strip() for line in f.readlines()]
start = [x for x in lines[0]]
pairs = dict(line.split(" -> ")  for line in lines[2:])

steps = 10
for _ in range(steps):
	new_list = []
	for i in range(len(start)-1):
		new_list.append(start[i])
		if start[i]+start[i+1] in pairs:
			new_list.append(pairs[start[i]+start[i+1]])
	new_list.append(start[-1])
	start = new_list

c = Counter(start).most_common()
res = c[0][1] - c[-1][1]
print(res)