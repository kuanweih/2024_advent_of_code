import re


def find_mul_expressions(text):
    # Pattern explanation:
    # mul        - matches literal 'mul'
    # \(         - matches opening parenthesis
    # (\d{1,3})  - matches 1-3 digits, captures in group 1
    # ,          - matches literal comma
    # (\d{1,3})  - matches 1-3 digits, captures in group 2
    # \)         - matches closing parenthesis
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    # Find all matches in the text
    matches = re.findall(pattern, text)

    return matches


if __name__ == "__main__":

    file_path = "./inputs/03.txt"

    with open(file_path, "r", encoding="utf-8") as file:
        strings = [line.strip() for line in file]

    result = 0
    for string in strings:
        matches = find_mul_expressions(string)
        for num1, num2 in matches:
            result += int(num1) * int(num2)

    print(result)
