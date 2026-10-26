def modefiedMatrix(matrix: list[list[int]], avg: float) -> list[list[int | str]]:
    newMatrix: list[list[int | str]] = []
    for line in matrix:
        newLine: list[int | str] = []
        for object in line:
            if object < avg:
                newLine.append("x")
            elif object % 2 == 1:
                newLine.append("y")
            else:
                newLine.append(object)
        newMatrix.append(newLine)
    return newMatrix


matrix: list[list[int]] = []
with open("inputMatrix.txt", "r") as input:
    N = int(input.readline())
    M = int(input.readline())
    for number in range(M):
        textIn = input.readline().split(" ")
        if len(textIn) != N:
            raise TypeError("Size of given array is different from given N")
        matrix.append([int(x) for x in textIn])

evenNumbers = 0
countEven = 0
with open("output.txt", "w") as output:
    for line in matrix:
        for object in line:
            _ = output.write(f"{object} ")
        _ = output.write(f"\n")
    _ = output.write("\n")
    for numberOfColumn in range(N):
        column: list[int] = []
        for numberOfLine in range(M):
            column.append(matrix[numberOfLine][numberOfColumn])
        _ = output.write(f"{min(column)} ")
    _ = output.write(f"\n")
    for line in matrix:
        for object in line:
            if object % 2 == 0:
                evenNumbers += object
                countEven += 1
    avgEven = evenNumbers / countEven
    _ = output.write(f"{avgEven}\n")
