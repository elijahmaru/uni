from random import randint

fileName = input("Введите название файла: ")
with open(f"{fileName}.txt", "w") as output:
    N = int(input("Введите кол-во столбцов: "))
    M = int(input("Введите кол-во строк: "))
    _ = output.write(f"{N}\n{M}\n")
    for _ in range(M):
        textOut: list[str] = []
        for _ in range(N):
            textOut.append(str(randint(-1000, 1000)))
        _ = output.write(" ".join(textOut) + "\n")
