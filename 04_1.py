file_path = "./inputs/04.txt"

with open(file_path, "r", encoding="utf-8") as file:
    matrix = [list(line.strip()) for line in file]


R = len(matrix)
C = len(matrix[0])
TARGET = "XMAS"


def dfs(target_id, r, c, dr, dc):
    if target_id == len(TARGET):
        return True
    nr = r + dr
    nc = c + dc
    if nr < 0 or nr >= R or nc < 0 or nc >= C:
        return False
    if matrix[nr][nc] != TARGET[target_id]:
        return False
    return dfs(target_id + 1, nr, nc, dr, dc)


if __name__ == "__main__":

    result = 0
    for r in range(R):
        for c in range(C):
            if matrix[r][c] != "X":
                continue

            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue

                    if dfs(1, r, c, dr, dc):
                        result += 1

    print(result)
