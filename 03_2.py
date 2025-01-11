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


def find_exact_matches(text, patterns):
    results = {}
    for pattern in patterns:
        matches = [(m.start(), m.end()) for m in re.finditer(pattern, text)]
        if matches:
            results[pattern] = matches

    return results


if __name__ == "__main__":

    file_path = "./inputs/03.txt"

    with open(file_path, "r", encoding="utf-8") as file:
        strings = [line.strip() for line in file]

    string = "".join(strings)

    result = 0

    string = "do()" + string

    patterns = ["do()", "don't()"]
    matches = find_exact_matches(string, patterns)

    delimiter_starts = []
    for pattern, positions in matches.items():
        for start, end in positions:
            delimiter_starts.append(start)
    delimiter_starts.sort()

    substrings = [
        string[i:j] for i, j in zip(delimiter_starts, delimiter_starts[1:] + [None])
    ]

    for substring in substrings:
        if substring.startswith("do()"):

            matches = find_mul_expressions(substring)
            for num1, num2 in matches:
                result += int(num1) * int(num2)

    print(result)
