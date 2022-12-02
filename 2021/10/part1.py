with open("10\\input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

pairs = {
    "[": "]",
    "{": "}",
    "(": ")",
    "<": ">"
}

bracket_vals = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

def validate_line(line): 
    opening = []
    for char in line:
        if char in pairs.keys():
            opening.append(char)
        elif char in bracket_vals.keys():
            if pairs[opening.pop()] != char:
                return char

wrong_chars = [validate_line(line) for line in lines if validate_line(line)]

print(sum(bracket_vals[char] for char in wrong_chars))