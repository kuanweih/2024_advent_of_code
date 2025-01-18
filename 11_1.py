def read_input(file_path):
    res = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            res.append(list(map(int, line.strip().split())))
    return res[0]


file_path = "./inputs/11.txt"
stones = read_input(file_path)


def blink(stones):
    res = []
    for stone in stones:
        if stone == 0:
            res.append(1)
        elif len(str(stone)) % 2 == 0:
            half = len(str(stone)) // 2
            left = int(str(stone)[:half])
            right = int(str(stone)[half:])
            res.append(left)
            res.append(right)

        else:
            res.append(stone * 2024)
    return res


for _ in range(25):
    stones = blink(stones)

print(len(stones))
