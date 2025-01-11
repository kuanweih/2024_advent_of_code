if __name__ == "__main__":

    file_path = "./inputs/04.txt"

    with open(file_path, "r", encoding="utf-8") as file:
        matrix = [list(line.strip()) for line in file]

    R = len(matrix)
    C = len(matrix[0])

    result = 0
    for r in range(R):
        for c in range(C):
            if matrix[r][c] != "A":
                continue
            if r == 0 or r == R - 1 or c == 0 or c == C - 1:
                continue

            check_diagonal_1 = (matrix[r - 1][c - 1] == "M" and matrix[r + 1][c + 1] == "S") or (matrix[r - 1][c - 1] == "S" and matrix[r + 1][c + 1] == "M")
            check_diagonal_2 = (matrix[r - 1][c + 1] == "M" and matrix[r + 1][c - 1] == "S") or (matrix[r - 1][c + 1] == "S" and matrix[r + 1][c - 1] == "M")

            if check_diagonal_1 and check_diagonal_2:
                result += 1

    print(result)
