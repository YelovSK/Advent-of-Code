with open("10\\input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

pairs = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

bracket_vals = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

def score_incomplete(line):
    score = 0
    opening = []
    for char in line:
        if char in pairs.keys():
            opening.insert(0, char)
        elif pairs[opening.pop(0)] != char:
            return 0
    for char in opening:
        score *= 5
        score += bracket_vals[pairs[char]]
    return score

scores = [score for line in lines if (score := score_incomplete(line))] # uwu what's diz
print(sorted(scores)[len(scores) // 2])