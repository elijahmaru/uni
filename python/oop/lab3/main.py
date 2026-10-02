def func(number: int) -> float:
    if number % 2 == 1:
        added = X**(number*2)
    else:
        added = -(Y**(number*2))
    added /= (number * 2 - 1) * (number * 2 + 1)
    return added


with open("input.txt", "r") as input:
    X = float(input.readline())
    Y = float(input.readline())
    N = int(input.readline())
    t = int(input.readline())


z = 0.0
textOut = ""
match t:
    case 0:
        for num in range(1, N + 1):
            z += func(num)
        textOut = str(z)
    case 1:
        number = 1
        while number <= N:
            z += func(number)
            number += 1
        textOut = str(z)
    case 2:
        number = 1
        while True:
            z += func(number)
            number += 1
            if number == N:
                break
    case _:
        textOut = "t wrong type. It can only be 0, 1 or 2"

with open("output.txt", "w") as output:
    _ = output.write(textOut)
