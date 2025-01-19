import collections


def read_input(file_path):
    res = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            res.append([ch for ch in line.strip()])
    return res


file_path = "./inputs/12.txt"
garden = read_input(file_path)


R = len(garden)
C = len(garden[0])


def bfs(r, c):
    plant = garden[r][c]
    queue = collections.deque()
    queue.append((r, c))
    garden[r][c] = None
    area = 0
    horizontals = collections.Counter()
    verticals = collections.Counter()

    while queue:
        r, c = queue.popleft()
        area += 1
        horizontals[(r, c)] += 1
        horizontals[(r + 1, c)] += 1
        verticals[(r, c)] += 1
        verticals[(r, c + 1)] += 1
        for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= nr < R and 0 <= nc < C and garden[nr][nc] == plant:
                queue.append((nr, nc))
                garden[nr][nc] = None

    perimeter = sum(cnt == 1 for cnt in horizontals.values())
    perimeter += sum(cnt == 1 for cnt in verticals.values())
    return area, perimeter


price = 0
for r in range(R):
    for c in range(C):
        if garden[r][c] is None:
            continue
        area, perimeter = bfs(r, c)
        price += area * perimeter

print(price)
