from enum import Enum

WIN_SCORE = 6
DRAW_SCORE = 3
LOSE_SCORE = 0

ROCK_SCORE = 1
PAPER_SCORE = 2
SCISSORS_SCORE = 3

class RPC(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

def get_rpc(char: str) -> RPC:
    if char == "X" or char == "A":
        return RPC.ROCK
    elif char == "Y" or char == "B":
        return RPC.PAPER
    elif char == "Z" or char == "C":
        return RPC.SCISSORS

def get_score(opponent: RPC, player: RPC) -> int:
    if opponent == player:
        return DRAW_SCORE

    if opponent == RPC.ROCK:
        return WIN_SCORE if player == RPC.PAPER else LOSE_SCORE
    elif opponent == RPC.PAPER:
        return WIN_SCORE if player == RPC.SCISSORS else LOSE_SCORE
    elif opponent == RPC.SCISSORS:
        return WIN_SCORE if player == RPC.ROCK else LOSE_SCORE

with open("02/input.txt", "r") as f:
    data = f.readlines()

# Strip newlines
data = [d.strip() for d in data]
# Split into pairs
pairs = [d.split(" ") for d in data]
# Strings into RPCs
pairs = [(get_rpc(p[0]), get_rpc(p[1])) for p in pairs]

score = 0
for opponent, player in pairs:
    if player == RPC.ROCK:
        score += ROCK_SCORE
    elif player == RPC.PAPER:
        score += PAPER_SCORE
    elif player == RPC.SCISSORS:
        score += SCISSORS_SCORE

    score += get_score(opponent, player)

print("Part 1:", score)