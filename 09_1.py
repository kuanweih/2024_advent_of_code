def read_input(file_path):
    res = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            res.append(line.strip())
    return res[0]


file_path = "./inputs/09.txt"
disk_map = read_input(file_path)

disk_size = sum(int(ch) for ch in disk_map)

filesystem = []
for i, ch in enumerate(disk_map):
    if i % 2 == 0:
        ifile = i // 2
        for _ in range(int(ch)):
            filesystem.append(int(ifile))
    else:
        for _ in range(int(ch)):
            filesystem.append(-1)


l = 0
r = len(filesystem) - 1
while l < r:
    while l < r and filesystem[l] != -1:
        l += 1
    while l < r and filesystem[r] == -1:
        r -= 1
    if l < r:
        filesystem[l], filesystem[r] = filesystem[r], filesystem[l]
        l += 1
        r -= 1

res = sum(i * x for i, x in enumerate(filesystem) if x != -1)

print(res)
