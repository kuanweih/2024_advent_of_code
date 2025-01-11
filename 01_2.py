import collections


if __name__ == "__main__":

    file_path = "./inputs/01.txt"

    with open(file_path, "r", encoding="utf-8") as file:
        input_lines = [line.strip().replace("   ", " ").split(" ") for line in file]

    list1 = []
    list2 = []
    for line in input_lines:
        list1.append(int(line[0]))
        list2.append(int(line[1]))

    counter2 = collections.Counter(list2)

    result = 0
    for x in list1:
        cnt = counter2[x]
        result += x * cnt

    print(result)
