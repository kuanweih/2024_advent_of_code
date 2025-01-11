import functools


cache = {}

def is_ordered(update):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            key = (update[i], update[j])
            if key in cache and cache[key] == 1:
                return False
    return True


def cmp(x, y):
    return cache.get((x, y), 0)




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
    
    for x, y in rules:
        cache[(x, y)] = -1
        cache[(y, x)] = 1
        
    print(cache)
    
    res = 0
    for update in updates:
        if is_ordered(update):
            continue
        
        update.sort(key=functools.cmp_to_key(cmp))
        
        middle = update[len(update) // 2]
        res += middle        
    


    

    print(res)
