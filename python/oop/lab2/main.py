from math import sqrt

with open("input.txt", "r") as input:
    a_71 = float(input.readline())
    _u2 = float(input.readline())
    test = float(input.readline())
    zoo = float(input.readline())
    x = float(input.readline())

with open("output.txt", "w") as output:
    if x == 0 or (a_71 - zoo == 0) or _u2 - test < 0:
        my_tmp = "ERROR"
    else:
        my_tmp = a_71 * sqrt((_u2 - test) / x) * (zoo / (a_71 - zoo))
    if _u2 == 0:
        geo = "ERROR"
    else:
        geo = sqrt(x / _u2) * (a_71) ** 2 * test
    if type(my_tmp) == str:
        _ = output.write(f"{my_tmp}\n")
    else:
        _ = output.write(f"{my_tmp:.2f}\n")
    if type(geo) == str:
        _ = output.write(f"{geo}\n")
    else:
        _ = output.write(f"{geo:.2f}\n")
