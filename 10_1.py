import collections


def read_input(file_path):
    res = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            res.append(list(map(int, line.strip())))
    return res


file_path = "./inputs/10.txt"
heights = read_input(file_path)


R = len(heights)
C = len(heights[0])


score = 0
for r0 in range(R):
    for c0 in range(C):
        if heights[r0][c0] != 0:
            continue

        queue = collections.deque()
        queue.append((r0, c0))
        seen = {(r0, c0)}
        ends = set()
        while queue:
            r, c = queue.popleft()
            if heights[r][c] == 9:
                ends.add((r, c))
                continue

            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if (
                    0 <= nr < R
                    and 0 <= nc < C
                    and (nr, nc) not in seen
                    and heights[nr][nc] == heights[r][c] + 1
                ):
                    seen.add((nr, nc))
                    queue.append((nr, nc))

        score += len(ends)

print(score)
