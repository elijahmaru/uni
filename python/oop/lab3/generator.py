from random import randint

fileName = input("Введите название файла: ")
with open(f"{fileName}.txt", "w") as output:
    N = int(input("Введите кол-во чисел: "))
    _ = output.write(str(N) + "\n")
    textOut: list[str] = []
    for _ in range(N):
        textOut.append(str(randint(-100, 100)))
    _ = output.write(" ".join(textOut))
