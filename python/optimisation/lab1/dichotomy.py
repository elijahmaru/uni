from typing import Callable


def dichotomy(
    start: float,
    end: float,
    numberOfIterations: int,
    epsilon: float,
    function: Callable[[float], float],
):
    for _ in range(numberOfIterations // 2):
        mid: float = (start + end) / 2
        xLeft, xRight = mid - epsilon / 2, mid + epsilon / 2
        print(f"Точки:\nx1 = {xLeft}\nx2 = {xRight}")
        if function(xLeft) < function(xRight):
            print(
                f"Значение в т. x1 = {xLeft} меньше => меняем a = x2 = {function(xRight)}"
            )
            end = xRight
        else:
            start = xLeft
            print(
                f"Значение в т. x2 = {xRight} меньше => меняем a = x1 = {function(xLeft)}"
            )
    graph = {
        start: function(start),
        start + epsilon: function(start + epsilon),
        end - epsilon: function(end - epsilon),
        end: function(end),
    }
    return min(graph.items(), key=lambda item: item[1])
