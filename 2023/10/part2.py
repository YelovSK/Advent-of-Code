import sys
from PIL import Image

with open("2023/10/test_input.txt") as f:
    data = f.read().strip()


map = dict()

lines = data.splitlines()

ABOVE_CONNECTIONS = ("7", "F", "|", "S")
BELOW_CONNECTIONS = ("L", "J", "|", "S")
LEFT_CONNECTIONS = ("L", "F", "-", "S")
RIGHT_CONNECTIONS = ("7", "J", "-", "S")

def get_connections(x, y):
    c = lines[x][y]
    res = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                continue

            if i != 0 and j != 0:
                continue

            xx = x + i
            yy = y + j

            if xx < 0 or yy < 0:
                continue

            if xx >= len(lines) or yy >= len(lines[0]):
                continue

            cc = lines[xx][yy]
            if cc == ".":
                continue

            if xx == x - 1 and c in ("|", "L", "J", "S") and cc in ABOVE_CONNECTIONS:
                res.append((xx, yy))
            elif xx == x + 1 and c in ("|", "7", "F", "S") and cc in BELOW_CONNECTIONS:
                res.append((xx, yy))
            elif yy == y - 1 and c in ("-", "7", "J", "S") and cc in LEFT_CONNECTIONS:
                res.append((xx, yy))
            elif yy == y + 1 and c in ("-", "F", "L", "S") and cc in RIGHT_CONNECTIONS:
                res.append((xx, yy))

    return res

start = None

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == ".":
            continue
        map[(i, j)] = get_connections(i, j)
        if char == "S":
            start = (i, j)

# Find longest path from start (cannot visit same node twice)
def dfs(node, visited):
    if node in visited:
        return []

    visited.add(node)

    longest_path = []
    for child in map[node]:
        path = dfs(child, visited)
        if len(path) > len(longest_path):
            longest_path = path

    visited.remove(node)

    return [node] + longest_path


sys.setrecursionlimit(10**6)
r = dfs(start, set())

def flood_fill(matrix, x, y):
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] == 1:
        return

    matrix[x][y] = 1  # Mark the pixel as visited

    # Recursively fill neighboring pixels
    flood_fill(matrix, x + 1, y)
    flood_fill(matrix, x - 1, y)
    flood_fill(matrix, x, y + 1)
    flood_fill(matrix, x, y - 1)

def count_inner_pixels(coordinates):
    # Find the bounding box of the loop
    min_x = min(coord[0] for coord in coordinates)
    max_x = max(coord[0] for coord in coordinates) * 2
    min_y = min(coord[1] for coord in coordinates)
    max_y = max(coord[1] for coord in coordinates) * 2

    # Create a matrix to represent the pixels
    matrix = [[0] * (max_y - min_y + 1) for _ in range(min_x, max_x + 1)]

    for x, line in enumerate(matrix):
        for y, c in enumerate(line):
            if x % 2 != 0 or y % 2 != 0:
                continue

            xx = (x) // 2
            yy = (y) // 2
            if (xx, yy) not in coordinates:
                matrix[x - min_x][y - min_y] = 2

    # Mark the pixels inside the loop as 1
    for x, y in coordinates:
        xx = x * 2
        yy = y * 2
        c = lines[x][y]
        matrix[xx - min_x][yy - min_y] = 1
        # set surrounding to 1 if they are directly connected
        # (--), (||), (L|), (L-), etc
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == j == 0:
                    continue

                if i != 0 and j != 0:
                    continue

                xxx = x + i
                yyy = y + j

                if xxx < 0 or yyy < 0:
                    continue

                if xxx >= len(lines) or yyy >= len(lines[0]):
                    continue

                cc = lines[xxx][yyy]
                if cc == ".":
                    continue

                # print(c, cc)

                if xxx == x - 1 and c in ("|", "L", "J", "S") and cc in ABOVE_CONNECTIONS:
                    matrix[xx + i - min_x][yy + j - min_y] = 1
                elif xxx == x + 1 and c in ("|", "7", "F", "S") and cc in BELOW_CONNECTIONS:
                    matrix[xx + i - min_x][yy + j - min_y] = 1
                elif yyy == y - 1 and c in ("-", "7", "J", "S") and cc in LEFT_CONNECTIONS:
                    matrix[xx + i - min_x][yy + j - min_y] = 1
                elif yyy == y + 1 and c in ("-", "F", "L", "S") and cc in RIGHT_CONNECTIONS:
                    matrix[xx + i - min_x][yy + j - min_y] = 1

    img = create_image(matrix)
    img.save("2023/10/output.png")

    # Initialize the count of inner pixels
    inner_pixel_count = 0

    print("-" * 30)

    # Perform flood fill from an arbitrary point inside the inner part of the loop
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[0]) - 1):
            if matrix[i][j] == 0:
                inner_pixel_count += 1
                flood_fill(matrix, i, j)  # Flood fill from the inner pixel

    for line in matrix:
        print(line)

    return inner_pixel_count

def create_image(matrix):
    height = len(matrix)
    width = len(matrix[0])

    # Create a blank image with black background
    img = Image.new('RGB', (width, height), color='black')
    pixels = img.load()

    # Set pixel colors based on the matrix
    for i in range(height):
        for j in range(width):
            if matrix[i][j] == 1:
                pixels[j, i] = (255, 255, 255)  # White for 1s
            elif matrix[i][j] == 2:
                pixels[j, i] = (100, 100, 100)

    return img

result = count_inner_pixels(r)
print("Number of inner pixels:", result)

print("Part 2", len(r) // 2)
