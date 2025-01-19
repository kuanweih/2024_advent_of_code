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

print(R)
print(C)


def bfs(r, c):
    plant = garden[r][c]
    queue = collections.deque()
    queue.append((r, c))
    garden[r][c] = None
    area = 0
    horizontals = collections.defaultdict(list)
    verticals = collections.defaultdict(list)

    while queue:
        r, c = queue.popleft()
        area += 1
        horizontals[(r, c)].append(-1)
        horizontals[(r + 1, c)].append(1)
        verticals[(r, c)].append(-1)
        verticals[(r, c + 1)].append(1)
        for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= nr < R and 0 <= nc < C and garden[nr][nc] == plant:
                queue.append((nr, nc))
                garden[nr][nc] = None

    horizontals = [
        (r, c, dirs[0]) for (r, c), dirs in horizontals.items() if len(dirs) == 1
    ]
    verticals = [
        (c, r, dirs[0]) for (r, c), dirs in verticals.items() if len(dirs) == 1
    ]
    horizontals.append((float("-inf"), float("-inf"), 0))
    verticals.append((float("-inf"), float("-inf"), 0))
    horizontals.sort()
    verticals.sort()

    side = 0
    for i in range(1, len(horizontals)):
        pr, pc, pd = horizontals[i - 1]
        r, c, d = horizontals[i]
        if (r, c, d) != (pr, pc + 1, pd):
            side += 1
    for i in range(1, len(verticals)):
        pc, pr, pd = verticals[i - 1]
        c, r, d = verticals[i]
        if (r, c, d) != (pr + 1, pc, pd):
            side += 1

    return area, side


price = 0
for r in range(R):
    for c in range(C):
        if garden[r][c] is None:
            continue
        area, side = bfs(r, c)
        price += area * side

print(price)
