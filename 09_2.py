import collections


def read_input(file_path):
    res = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            res.append(line.strip())
    return res[0]


file_path = "./inputs/09.txt"
disk_map = read_input(file_path)

blocks = []
spaces = []
for i, ch in enumerate(disk_map):
    if i % 2 == 0:
        blocks.append(int(ch))
    else:
        spaces.append(int(ch))


# print(blocks)
# print(spaces)
# print(len(blocks))
# print(len(spaces))

block_to_space = {}
space_to_block = collections.defaultdict(list)

for b in range(len(blocks) - 1, -1, -1):
    for s in range(len(spaces)):
        if spaces[s] >= blocks[b]:
            block_to_space[b] = s
            space_to_block[s].append(b)
            spaces[s] -= blocks[b]
            break

print(block_to_space)
print(space_to_block)
print(blocks)
print(spaces)

filesystem = []
for i in range(len(blocks)):
    if i not in block_to_space:
        for _ in range(blocks[i]):
            filesystem.append(i)
    else:
        for _ in range(blocks[i]):
            filesystem.append(-1)

    if i == len(spaces):
        break

    if i in space_to_block:
        for b in space_to_block[i]:
            for _ in range(blocks[b]):
                filesystem.append(b)
    for _ in range(spaces[i]):
        filesystem.append(-1)

print(filesystem)

res = sum(i * x for i, x in enumerate(filesystem) if x != -1)

print(res)



# 8551696246309 too high
