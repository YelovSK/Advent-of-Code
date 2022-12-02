from enum import IntEnum


class RPC(IntEnum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Result(IntEnum):
    WIN = 6
    DRAW = 3
    LOSE = 0

rpc_map = {
    "A": RPC.ROCK,
    "B": RPC.PAPER,
    "C": RPC.SCISSORS,
}
result_map = {
    "X": Result.LOSE,
    "Y": Result.DRAW,
    "Z": Result.WIN,
}

def get_player(opponent: RPC, result: Result) -> RPC:
    if result == Result.DRAW:
        return opponent

    if opponent == RPC.ROCK:
        return RPC.PAPER if result == Result.WIN else RPC.SCISSORS
    elif opponent == RPC.PAPER:
        return RPC.SCISSORS if result == Result.WIN else RPC.ROCK
    elif opponent == RPC.SCISSORS:
        return RPC.ROCK if result == Result.WIN else RPC.PAPER

with open("02/input.txt", "r") as f:
    data = [l.strip() for l in f.readlines()]

score = 0
for opponent, result in [row.split(" ") for row in data]:
    result = result_map[result]
    opponent = rpc_map[opponent]

    score += result
    score += get_player(opponent, result)

print("Part 2:", score)