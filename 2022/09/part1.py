with open("09/input.txt") as f:
    data = [l.strip() for l in f.readlines()]

directions = {
    "L": (-1, 0),
    "R": (1, 0),
    "U": (0, -1),
    "D": (0, 1),
}

TAIL_COUNT = 1
tail_history = set()
snake = [(0, 0) for _ in range(1 + TAIL_COUNT)]

for line in data:
    direction, count = line.split()
    x, y = directions[direction]

    for i in range(int(count)):
        # Move head
        snake[0] = (snake[0][0] + x, snake[0][1] + y)
        for ix, tail in enumerate(snake[1:]):
            ix += 1
            previous = snake[ix-1]

            x_diff = previous[0] - tail[0]
            y_diff = previous[1] - tail[1]

            move_by_x = 0
            move_by_y = 0

            # Horizontal
            if abs(x_diff) == 2 and abs(y_diff) == 0:
                move_by_x = 1 if x_diff > 0 else -1
            # Vertical
            elif abs(y_diff) == 2 and abs(x_diff) == 0:
                move_by_y = 1 if y_diff > 0 else -1
            # Diagonal
            elif abs(x_diff) == 2 and abs(y_diff) >= 1 or abs(y_diff) == 2 and abs(x_diff) >= 1:
                move_by_x = 1 if x_diff > 0 else -1
                move_by_y = 1 if y_diff > 0 else -1

            # Move
            tail = (tail[0] + move_by_x, tail[1] + move_by_y)

            # Update
            snake[ix] = tail
            tail_history.add(snake[-1])

print("Part 1:", len(tail_history))