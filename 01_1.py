if __name__ == "__main__":

    file_path = "./inputs/01.txt"

    with open(file_path, "r", encoding="utf-8") as file:
        input_lines = [line.strip().replace("   ", " ").split(" ") for line in file]

    list1 = []
    list2 = []
    for line in input_lines:
        list1.append(int(line[0]))
        list2.append(int(line[1]))

    list1.sort()
    list2.sort()

    result = 0
    for x1, x2 in zip(list1, list2):
        result += abs(x1 - x2)

    print(result)
