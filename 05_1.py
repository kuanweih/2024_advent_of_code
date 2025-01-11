
def is_ordered(update, cache):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            key = (update[i], update[j])
            if key in cache and not cache[key]:
                return False
    return True


if __name__ == "__main__":

    file_path = "./inputs/05.txt"

    rules = []
    updates = []
    with open(file_path, "r", encoding="utf-8") as file:
        res = rules
        for line in file:
            line = line.strip()
            if line == "":
                res = updates
                continue
            res.append(line)

    updates = [list(map(int, update.split(","))) for update in updates]
    rules = [list(map(int, rule.split("|"))) for rule in rules]
    
    cache = {}
    for x, y in rules:
        cache[(x, y)] = True
        cache[(y, x)] = False
        

    print(rules)
    print(updates)
    
    res = 0
    for update in updates:
        if is_ordered(update, cache):
            middle = update[len(update) // 2]
            res += middle        
    


    

    print(res)
