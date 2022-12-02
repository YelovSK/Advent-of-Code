from enum import IntEnum

class Result(IntEnum):
    WIN = 6
    DRAW = 3
    LOSE = 0

class RPC(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

rpc_map = {
    "A": RPC.ROCK,
    "X": RPC.ROCK,

    "B": RPC.PAPER,
    "Y": RPC.PAPER,

    "C": RPC.SCISSORS,
    "Z": RPC.SCISSORS,
}

def get_score(opponent: RPC, player: RPC) -> int:
    if opponent == player:
        return Result.DRAW

    if opponent == RPC.ROCK:
        return Result.WIN if player == RPC.PAPER else Result.LOSE
    elif opponent == RPC.PAPER:
        return Result.WIN if player == RPC.SCISSORS else Result.LOSE
    elif opponent == RPC.SCISSORS:
        return Result.WIN if player == RPC.ROCK else Result.LOSE

with open("02/input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

# Split into pairs
pairs = [d.split(" ") for d in data]

score = 0
for opponent, player in [row.split(" ") for row in data]:
    opponent = rpc_map[opponent]
    player = rpc_map[player]

    score += player
    score += get_score(opponent, player)

print("Part 1:", score)