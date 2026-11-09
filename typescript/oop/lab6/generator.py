from random import randint

with open(f"input.txt", "w") as output:
    N = int(input("Введите кол-во столбцов: "))
    M = int(input("Введите кол-во строк: "))
    for _ in range(M):
        textOut: list[str] = []
        for _ in range(N):
            textOut.append(str(randint(-1000, 1000)))
        _ = output.write(" ".join(textOut) + "\n")
