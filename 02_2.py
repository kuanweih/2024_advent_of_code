def check_safety(array):
    prev = array[0]
    orient = array[1] - array[0]
    for x in array[1:]:
        dx = x - prev
        if not 1 <= abs(dx) <= 3:
            return False
        if dx * orient < 0:
            return False
        prev = x
    return True


if __name__ == "__main__":

    file_path = "./inputs/02.txt"

    with open(file_path, "r", encoding="utf-8") as file:
        arrays = [list(map(int, line.strip().split(" "))) for line in file]

    print(len(arrays))

    result = 0
    for original_array in arrays:
        arrays_to_check = [original_array]
        for i in range(len(original_array)):
            adjusted_array = original_array[:i] + original_array[i + 1 :]
            arrays_to_check.append(adjusted_array)

        for array in arrays_to_check:
            if check_safety(array):
                result += 1
                break

    print(result)
