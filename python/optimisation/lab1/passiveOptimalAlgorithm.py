from typing import Callable


def passive(
    start: float,
    end: float,
    numberOfIteration: int,
    function: Callable[[float], float],
):
    m = numberOfIteration // 2 + 1
    graph: dict[float, float] = {}
    for j in range(1, m):
        x = start + j * (end - start) / m
        graph[x] = function(x)
    xMin, yMin = min(graph.items(), key=lambda item: item[1])
    return xMin, yMin, list(graph.keys())
