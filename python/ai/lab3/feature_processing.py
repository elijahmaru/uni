import math
import random
from typing import Callable


def _checkType(data: list[int]) -> bool:
    if len(data) == 0:
        raise TypeError("function didn't receive list of ints")
    if isinstance(data, list) and all(type(x) is int for x in data):
        return True
    raise TypeError("function didn't receive list of ints")


# task 1
def mean(data: list[int]) -> float:
    _checkType(data)
    sum = 0
    count = 0
    for i in data:
        sum += i
        count += 1
    return sum / count


def quickSelect(data: list[int], n: int) -> int:
    _checkType(data)
    if len(data) == 1:
        return data[0]

    pivotPoint = random.choice(data)
    lowerThanPivot = [x for x in data if x < pivotPoint]
    higherThanPivot = [x for x in data if x > pivotPoint]
    pivotPoints = [x for x in data if x == pivotPoint]

    if n < len(lowerThanPivot):
        return quickSelect(lowerThanPivot, n)
    elif n < len(lowerThanPivot) + len(pivotPoints):
        return pivotPoints[0]
    else:
        return quickSelect(higherThanPivot, n - len(lowerThanPivot) - len(pivotPoints))


def median(data: list[int]) -> float:
    _checkType(data)
    """ my implementation O(n^n + n)
    dictionary = {}
    for value in data:
        strValue = str(value)
        dictionary[strValue] = (0, 0)
        for valueCurrent in data:
            if valueCurrent < value:
                dictionary[strValue] = (
                    dictionary[strValue][0] + 1,
                    dictionary[strValue][1],
                )
            elif value < valueCurrent:
                dictionary[strValue] = (
                    dictionary[strValue][0],
                    dictionary[strValue][1] + 1,
                )

    if len(data) % 2 != 0:
        for key, value in dictionary.items():
            if value[0] == value[1]:
                return float(key)
    valuesForMedain = []
    for key, value in dictionary.items():
        if abs(value[0] - value[1]) == 1:
            valuesForMedain.append(int(key))
    return sum(valuesForMedain) / len(valuesForMedain)
    """
    # quickselect implementation O(n)
    length = len(data)
    if length % 2 == 1:
        return quickSelect(data, length // 2)
    else:
        leftMedian = quickSelect(data, length // 2 - 1)
        rightMedian = quickSelect(data, length // 2)
        return (leftMedian + rightMedian) / 2


def variance(data: list[int]) -> float:
    _checkType(data)
    sumOfSquares = 0
    avg = mean(data)
    for value in data:
        sumOfSquares += (value - avg) ** 2
    return sumOfSquares / len(data)


def std(data: list[int]) -> float:
    _checkType(data)
    return variance(data) ** 0.5


# task 2
def min_max_scale(
    data: list[int], feature_range: tuple[int, int] = (0, 1)
) -> list[float]:
    _checkType(data)
    currentMin = min(data)
    currentMax = max(data)
    minVal = feature_range[0]
    maxVal = feature_range[1]
    return [
        minVal + (value - currentMin) * (maxVal - minVal) / (currentMax - currentMin)
        for value in data
    ]


def log_scale(data: list[int], base: float = math.e) -> list[float]:
    if _checkType(data) and not all(value > 0 for value in data):
        raise ValueError(
            "0 or negatives in array cannot perform conversion to log scale"
        )
    return [math.log(value, base) for value in data]


def standardize(data: list[int]) -> list[float]:
    _checkType(data)
    avg = mean(data)
    stdDeviation = std(data)
    return [(value - avg) / stdDeviation for value in data]


def remove_outliers(data: list[int], k) -> list[int]:
    _checkType(data)
    avg = mean(data)
    stdDeviation = std(data)
    return [value for value in data if abs(value - avg) <= (stdDeviation * k)]


def apply_pipeline(
    data: list[int], transformations: list[Callable]
) -> list[float] | list[int]:
    finalList = [value for value in data]
    for func in transformations:
        try:
            finalList = func(data)
        except Exception as e:
            if e == "function didn't receive list of ints":
                print(e)
            elif e == "0 or negatives in array cannot perform conversion to log scale":
                print(
                    "Was unable do convert to log scale proceded without converstion\nError: ",
                    e,
                )
    return finalList
