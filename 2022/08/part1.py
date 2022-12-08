def is_visible(row_ix: int, column_ix: int) -> int:
    # Visible if on the edge
    if row_ix == 0 or row_ix == len(grid) - 1:
        return True
    if column_ix == 0 or column_ix == len(grid[row_ix]) - 1:
        return True

    value = grid[row_ix][column_ix]
    row = grid[row_ix]
    column = [grid[row_ix][column_ix] for row_ix in range(len(grid))]

    left = all(x < value for x in row[:column_ix])
    right = all(x < value for x in row[column_ix + 1:])
    top = all(x < value for x in column[:row_ix])
    bottom = all(x < value for x in column[row_ix + 1:])

    return left or right or top or bottom


with open("08/input.txt") as f:
    data = [l.strip() for l in f.readlines()]

grid = [[int(x) for x in list(line)] for line in data]

count = sum([is_visible(row_ix, column_ix)
             for row_ix in range(len(grid))
             for column_ix in range(len(grid[row_ix]))])

print("Part 1:", count)
