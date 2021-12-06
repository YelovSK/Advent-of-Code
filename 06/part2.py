with open("06\\input.txt") as f:
    numbers = [int(x) for x in f.read().split(",")]

dict = {i: 0 for i in range(8+1)}
for number in numbers:
    dict[number] += 1

for _ in range(256):
    dict_cpy = dict.copy()
    for num in range(8+1):
        dict[num] = dict_cpy[0] if num == 8 else dict_cpy[num+1]
    dict[6] += dict_cpy[0]

print(sum(dict.values()))