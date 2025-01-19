import heapq


def read_input(file_path):
    res = []
    curr = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if line == "\n":
                res.append(curr)
                curr = []
                continue
            curr.append(line.strip())
    if curr:
        res.append(curr)
    return res


file_path = "./inputs/13.txt"
machines = read_input(file_path)


for i, machine in enumerate(machines):
    button_a = machine[0].split(":")[1].strip().split(",")
    button_b = machine[1].split(":")[1].strip().split(",")
    prize = machine[2].split(":")[1].strip().split(",")
    button_a = [int(x.replace("X+", "").replace("Y+", "").strip()) for x in button_a]
    button_b = [int(x.replace("X+", "").replace("Y+", "").strip()) for x in button_b]
    prize = [int(x.replace("X=", "").replace("Y=", "").strip()) for x in prize]
    machines[i] = {"A": button_a, "B": button_b, "P": prize}


def get_lowest_cost(machine):
    pq = [(0, 0, 0)]  # (cost, x, y)
    seen = set()  # (x, y)
    while pq:
        cost, x, y = heapq.heappop(pq)
        if x == machine["P"][0] and y == machine["P"][1]:
            return cost
        if (x, y) in seen or x > machine["P"][0] or y > machine["P"][1]:
            continue
        seen.add((x, y))
        for button in "AB":
            dx, dy = machine[button]
            dc = 3 if button == "A" else 1
            heapq.heappush(pq, (cost + dc, x + dx, y + dy))
    return 0


total = 0
for machine in machines:
    cost = get_lowest_cost(machine)
    total += cost

print(total)
