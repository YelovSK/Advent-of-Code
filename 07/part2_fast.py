with open("07\\input.txt") as f:
    positions = [int(x) for x in f.read().split(",")]

def calc_weight(num, positions):
    return sum(sum(range(1, abs(num-pos)+1)) for pos in positions)

avg = sum(positions) // len(positions)
print(sum(sum(range(1, abs(avg-pos)+1)) for pos in positions))