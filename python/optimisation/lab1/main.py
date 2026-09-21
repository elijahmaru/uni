from math import exp
from passiveOptimalAlgorithm import (  # pyright: ignore[reportImplicitRelativeImport]
    passive,
)
from dichotomy import dichotomy  # pyright: ignore[reportImplicitRelativeImport]
from goldenRatio import goldenRatio  # pyright: ignore[reportImplicitRelativeImport]


def function(x: float) -> float:
    return -4 * x + exp(abs(x - 0.2))


N: int = 24
epsilon: float = 0.1
a: float = 0.0
b: float = 2.0

print("\n\nПассивный оптимальный алгоритм")
resultOfPassive = passive(a, b, N, function)
print(
    f"Точка min значения x = {resultOfPassive[0]}\nMin значение y = {resultOfPassive[1]}\nПосчитанные точки {resultOfPassive[2]}"
)

print("\n\nМетод дихотомии")
resultOfDichotomy = dichotomy(a, b, N, epsilon, function)
print(
    f"Точка для min значения x = {resultOfDichotomy[0]}\nMin значение y = {resultOfDichotomy[1]}"
)

print("\n\nМетод золотого сечения")
resultOfGolden = goldenRatio(a, b, N, function)
print(
    f"Точка для min значения x = {resultOfGolden[0]}\nMin значение y = {resultOfGolden[1]}"
)
