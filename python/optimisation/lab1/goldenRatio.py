from math import sqrt
from typing import Callable


def goldenRatio(
    start: float,
    end: float,
    numberOfIterations: int,
    function: Callable[[float], float],
):
    phi = (1 + sqrt(5)) / 2
    x1 = end - (end - start) / phi
    x2 = start + (end - start) / phi
    y1 = function(x1)
    y2 = function(x2)
    for _ in range(numberOfIterations - 2):
        if y1 < y2:
            end = x2
            x2, y2 = x1, y1
            x1 = end - (end - start) / phi
            y1 = function(x1)
        else:
            start = x1
            x1, y1 = x2, y2
            x2 = start + (end - start) / phi
            y2 = function(x2)
    graph = {
        start: function(start),
        start + phi: function(start + phi),
        end - phi: function(end - phi),
        end: function(end),
    }
    return min(graph.items(), key=lambda item: item[1])
