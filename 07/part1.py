def calc_weight(num, positions):
    return sum(abs(num-pos) for pos in positions)

with open("07\\input.txt") as f:
    positions = [int(x) for x in f.read().split(",")]

weights = {pos: calc_weight(pos, positions) for pos in range(min(positions), max(positions)+1)}
weights = dict(sorted(weights.items(), key=lambda item: item[1]))

pos, weight = list(weights.items())[0]
print(f"Pos: {pos} | Weight: {weight}")