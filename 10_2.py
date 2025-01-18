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


ratings = 0
for r0 in range(R):
    for c0 in range(C):
        if heights[r0][c0] != 0:
            continue

        queue = collections.deque()
        queue.append((r0, c0))
        seen = collections.defaultdict(int)
        seen[(r0, c0)] += 1
        ends = collections.defaultdict(int)
        while queue:
            r, c = queue.popleft()
            if heights[r][c] == 9:
                ends[(r, c)] += seen[(r, c)]
                continue

            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < R and 0 <= nc < C and heights[nr][nc] == heights[r][c] + 1:
                    if (nr, nc) not in seen:
                        queue.append((nr, nc))
                    seen[(nr, nc)] += seen[(r, c)]

        ratings += sum(ends.values())

print(ratings)
