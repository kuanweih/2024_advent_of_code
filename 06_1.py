def read_input(file_path):
    grid = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = list(line.strip())
            grid.append(line)
    return grid


file_path = "./inputs/06.txt"
grid = read_input(file_path)

R = len(grid)
C = len(grid[0])
INIT_DIRECTIONS = {"v": (1, 0), "^": (-1, 0), "<": (0, -1), ">": (0, 1)}


def initialize(grid):
    for r in range(R):
        for c in range(C):
            if grid[r][c] in "^v<>":
                dr, dc = INIT_DIRECTIONS[grid[r][c]]
                return r, c, dr, dc


r, c, dr, dc = initialize(grid)


while True:
    nr = r + dr
    nc = c + dc
    if nr < 0 or nr >= R or nc < 0 or nc >= C:
        grid[r][c] = "X"
        break
    if grid[nr][nc] in ".X":
        grid[r][c] = "X"
        r, c = nr, nc
    elif grid[nr][nc] == "#":
        dr, dc = dc, -dr


res = 0
for r in range(R):
    for c in range(C):
        if grid[r][c] == "X":
            res += 1

print(res)
