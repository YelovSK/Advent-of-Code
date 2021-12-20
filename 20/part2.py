content = open("20\\input.txt").read()
algo = content.split()[0]
input = [list(line.strip()) for line in content.split()[1:]]

def get_index(input, x, y, outer):
    binary_res = ""
    for xx in range(x-1, x+2):
        for yy in range(y-1, y+2):
            try:
                curr = input[xx][yy]
            except IndexError:
                curr = outer
            if curr == ".":
                binary_res += "0"
            elif curr == "#":
                binary_res += "1"
    return int(binary_res, 2)

def get_new_output(input, ix):
    outer = "." if ix % 2 == 0 else "#"
    input.insert(0, [outer for _ in range(len(input[0]))])
    input.append([outer for _ in range(len(input[0]))])
    for r in input:
        r.insert(0, outer)
        r.append(outer)
    output = [[None for _ in range(len(input[0]))] for _ in range(len(input))]
    for x in range(len(input)):
        for y in range(len(input[x])):
            output[x][y] = algo[get_index(input, x, y, outer)]
    return output

res = list(input)
for ix in range(50):
    res = get_new_output(res, ix)
    
count = sum(r.count("#") for r in res)
print(count)