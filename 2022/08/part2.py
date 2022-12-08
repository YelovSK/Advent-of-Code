def get_score(row_ix: int, column_ix: int) -> int:
    value = grid[row_ix][column_ix]
    row = grid[row_ix]
    column = [grid[row_ix][column_ix] for row_ix in range(len(grid))]

    left, right, top, bottom = 0, 0, 0, 0

    # Check left
    for x in reversed(row[:column_ix]):
        left += 1
        if x >= value:
            break

    # Check right
    for x in row[column_ix + 1:]:
        right += 1
        if x >= value:
            break

    # Check top
    for x in reversed(column[:row_ix]):
        top += 1
        if x >= value:
            break

    # Check bottom
    for x in column[row_ix + 1:]:
        bottom += 1
        if x >= value:
            break

    return left * right * top * bottom


with open("08/input.txt") as f:
    data = [l.strip() for l in f.readlines()]

grid = [[int(x) for x in list(line)] for line in data]

result = max([get_score(row_ix, column_ix)
              for row_ix in range(len(grid))
              for column_ix in range(len(grid[row_ix]))])

print("Part 2:", result)
