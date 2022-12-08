def get_score(row_ix: int, column_ix: int) -> int:
    value = grid[row_ix][column_ix]
    row = grid[row_ix]
    column = [grid[row_ix][column_ix] for row_ix in range(len(grid))]

    left, right, top, bottom = 0, 0, 0, 0

    # Check left
    for x in reversed(row[:column_ix]):
        if x >= value:
            left += 1
            break
        left += 1

    # Check right
    for x in row[column_ix + 1:]:
        if x >= value:
            right += 1
            break
        right += 1

    # Check top
    for x in reversed(column[:row_ix]):
        if x >= value:
            top += 1
            break
        top += 1

    # Check bottom
    for x in column[row_ix + 1:]:
        if x >= value:
            bottom += 1
            break
        bottom += 1

    return left * right * top * bottom


with open("08/input.txt") as f:
    data = [l.strip() for l in f.readlines()]

grid = [[int(x) for x in list(line)] for line in data]

result = max([get_score(row_ix, column_ix)
              for row_ix in range(len(grid))
              for column_ix in range(len(grid[row_ix]))])

print("Part 2:", result)
