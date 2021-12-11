# read file
with open("04\\input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

# create boards
numbers = lines[0].split(",")
current_board = -1
boards = {}
for line in lines[1:]:
    if not line:
        current_board += 1
        boards[current_board] = []
    else:
        boards[current_board].append(line.split())

def check_board_completion(board):
    # horizontal
    for row in board:
        if len([1 for num in row if num[-1] == "m"]) == len(row):
            return True
    # vertical
    for i in range(5):
        column = [row[i] for row in board]
        if len([1 for num in column if num[-1] == "m"]) == len(column):
            return True
    return False

# mark numbers
def get_winning_boards():
    for number in numbers:
        for board_num, board in boards.items():
            for j, line in enumerate(board):
                for i, col in enumerate(line):
                    if col == number:
                        board[j][i] += "m"
            if check_board_completion(board):
                return board, int(number)
    return None

winning_board, number = get_winning_boards()
sum = 0
for row in winning_board:
    for column in row:
        if column[-1] != "m":
            sum += int(column)
print(f"Sum: {sum} | Last number: {number} | Result: {sum*number}")