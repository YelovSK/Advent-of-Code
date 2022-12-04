with open("04/input.txt") as f:
    data = [l.strip().split(",") for l in f.readlines()]

p1, p2 = 0, 0
for l, r in data:
    s1, e1 = map(int, l.split("-"))
    s2, e2 = map(int, r.split("-"))

    if s1 <= s2 and e1 >= e2 or s2 <= s1 and e2 >= e1:
        p1 += 1

    if not (e1 < s2 or e2 < s1):
        p2 += 1

print("Part 1:", p1)
print("Part 2:", p2)
