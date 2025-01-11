import collections


def read_input(file_path):
    res = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = list(line.strip())
            res.append(line)
    return res


file_path = "./inputs/08.txt"
grid = read_input(file_path)


def get_antinode_locations(ri, ci, rj, cj):
    dr = ri - rj
    dc = ci - cj
    r, c = ri, ci
    res = set()
    while 0 <= r < R and 0 <= c < C:
        res.add((r, c))
        r += dr
        c += dc
    return res


R = len(grid)
C = len(grid[0])

signals = collections.defaultdict(list)

for r in range(R):
    for c in range(C):
        if grid[r][c] != ".":
            signals[grid[r][c]].append((r, c))

antinodes = set()

for signal, locations in signals.items():
    if len(locations) == 1:
        continue
    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            ri, ci = locations[i]
            rj, cj = locations[j]
            antinodes = antinodes.union(
                get_antinode_locations(ri, ci, rj, cj),
                get_antinode_locations(rj, cj, ri, ci),
            )


print(len(antinodes))
