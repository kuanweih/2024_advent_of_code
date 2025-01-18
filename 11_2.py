import collections


def read_input(file_path):
    res = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            res.append(list(map(int, line.strip().split())))
    return res[0]


file_path = "./inputs/11.txt"
stones = read_input(file_path)

stones = collections.Counter(stones)

def blink(stones):
    res = collections.Counter()
    for stone, cnt in stones.items():
        if stone == 0:
            res[1] += cnt
        elif len(str(stone)) % 2 == 0:
            half = len(str(stone)) // 2
            left = int(str(stone)[:half])
            right = int(str(stone)[half:])
            res[left] += cnt
            res[right] += cnt
        else:
            res[stone * 2024] += cnt
    return res


for _ in range(75):
    stones = blink(stones)

print(sum(stones.values()))
