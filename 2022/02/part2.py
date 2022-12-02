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

class Result(Enum):
    WIN = 1
    DRAW = 2
    LOSE = 3

def get_rpc(char: str) -> RPC:
    if char == "A":
        return RPC.ROCK
    elif char == "B":
        return RPC.PAPER
    elif char == "C":
        return RPC.SCISSORS

def get_result(char: str) -> Result:
    if char == "X":
        return Result.LOSE
    elif char == "Y":
        return Result.DRAW
    elif char == "Z":
        return Result.WIN

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
    data = f.readlines()

# Strip newlines
data = [d.strip() for d in data]
# Split into pairs
pairs = [d.split(" ") for d in data]

score = 0
for opponent, result in pairs:
    result = get_result(result)

    if result == Result.WIN:
        score += WIN_SCORE
    elif result == Result.DRAW:
        score += DRAW_SCORE
    elif result == Result.LOSE:
        score += LOSE_SCORE

    opponent = get_rpc(opponent)
    player = get_player(opponent, result)

    if player == RPC.ROCK:
        score += ROCK_SCORE
    elif player == RPC.PAPER:
        score += PAPER_SCORE
    elif player == RPC.SCISSORS:
        score += SCISSORS_SCORE

print("Part 2:", score)