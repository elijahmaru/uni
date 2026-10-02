with open("input.txt", "r") as input:
    N = int(input.readline())
    textIn = input.readline().split(" ")
    if len(textIn) != N:
        raise TypeError("Size of given array is different from given N")


arrayOfSizeN = list(int(num) for num in textIn)
counter = 0
resultFirst = 1
for number in arrayOfSizeN:
    if number < 50:
        counter += 1
        resultFirst *= number
textOutFirst = str(resultFirst) if counter != 0 else "0"

avg = sum(arrayOfSizeN) / len(arrayOfSizeN)
resultSecond: list[str] = []
for number in arrayOfSizeN:
    if number > avg:
        resultSecond.append(str(number))
textOutSecond = " ".join(resultSecond)

with open("output.txt", "w") as output:
    _ = output.write(textOutFirst+"\n")
    _ = output.write(textOutSecond)
