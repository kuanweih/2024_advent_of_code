from sympy import symbols, solve, Eq


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


def solve_linear_system(Ax, Bx, Px, Ay, By, Py):
    """
    Solve a system of two linear equations:
    Ax * a + Bx * b = Px
    Ay * a + By *b = Py

    Args:
        Ax, Bx, Px: Coefficients and constant for first equation
        Ay, By, Py: Coefficients and constant for second equation

    Returns:
        dict: Solution with a and b values, or None if no solution exists
    """
    # Define the variables
    a, b = symbols("a b")

    # Create the equations
    eq1 = Eq(Ax * a + Bx * b, Px)
    eq2 = Eq(Ay * a + By * b, Py)

    # Solve the system
    solution = solve((eq1, eq2), (a, b))

    # Return the solution if it exists and is integer, otherwise return None
    return (
        (int(solution[a]), int(solution[b]))
        if solution and all(val.is_integer for val in solution.values())
        else None
    )

prize_offset = 10000000000000
total = 0
for machine in machines:
    solution = solve_linear_system(
        machine["A"][0],
        machine["B"][0],
        machine["P"][0] + prize_offset,
        machine["A"][1],
        machine["B"][1],
        machine["P"][1] + prize_offset,
    )

    a, b = solution if solution is not None else (0, 0)

    total += 3 * a + 1 * b

print(total)
