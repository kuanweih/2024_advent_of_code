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
            for nr, nc in [
                (2 * ri - rj, 2 * ci - cj),
                (2 * rj - ri, 2 * cj - ci),
            ]:
                if 0 <= nr < R and 0 <= nc < C:
                    antinodes.add((nr, nc))

print(len(antinodes))
