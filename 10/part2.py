with open("10\\input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

pairs = {
    "[": "]",
    "{": "}",
    "(": ")",
    "<": ">"
}

bracket_vals = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

def validate_line(line):
    opening = []
    for char in line:
        if char in pairs.keys():
            opening.append(char)
        elif char in bracket_vals.keys():
            if pairs[opening.pop()] != char:
                return char

def score_incomplete(line):
    score = 0
    opening = []
    for char in line:
        if char in pairs.keys():
            opening.insert(0, char)
        elif char in bracket_vals.keys():
            opening.pop(0)
    for char in opening:
        score *= 5
        score += bracket_vals[pairs[char]]
    return score

corrupted_lines = [line for line in lines if validate_line(line)]
for line in corrupted_lines:
    lines.remove(line)

scores = [score_incomplete(line) for line in lines]
print(sorted(scores)[len(scores)//2])