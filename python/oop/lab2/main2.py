from math import sqrt

with open("input.txt", "r") as input:
    a1 = float(input.readline())
    a2 = float(input.readline())
    a3 = float(input.readline())
    a4 = float(input.readline())
    a5 = float(input.readline())

with open("output.txt", "w") as target:
    try:
        s = a1 * sqrt(a2 - a3) * a4 / a5
    except ValueError as e:
        s = "ERROR"
    if type(s) == str:
        _ = target.write(f"{s}\n")
    else:
        _ = target.write(f"{s:.3f}\n")
