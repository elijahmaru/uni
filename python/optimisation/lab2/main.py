import matplotlib.pyplot as plt
import numpy as np

constraints = (
    (4, 5, 600, "Сырьё 1"),
    (6, 3, 540, "Сырьё 2"),
    (2, 0, 120, "Сырьё 3"),
)
profit = (6, 7)


def formatNumber(value: float) -> str:
    return str(int(round(value))) if np.isclose(value, round(value)) else f"{value:.2f}"


def printTableau(tableau: np.ndarray, basis: list[int], costs: np.ndarray) -> None:
    variableNames = ["x1", "x2", "s1", "s2", "s3"]
    header = ["Базис", "Cb", "b", *variableNames]
    rows: list[list[str]] = []

    for row, basicVariable in zip(tableau, basis):
        rows.append(
            [
                variableNames[basicVariable],
                formatNumber(costs[basicVariable]),
                formatNumber(row[-1]),
                *(formatNumber(value) for value in row[:-1]),
            ]
        )

    zj = costs[basis] @ tableau[:, :-1]
    reducedCosts = costs - zj
    rows.append(["Cj − Zj", "", "", *(formatNumber(value) for value in reducedCosts)])

    widths = [
        max(len(header[i]), *(len(row[i]) for row in rows)) for i in range(len(header))
    ]
    print("  ".join(title.rjust(widths[i]) for i, title in enumerate(header)))
    for row in rows:
        print("  ".join(cell.rjust(widths[i]) for i, cell in enumerate(row)))


def simplexMethod() -> tuple[float, float, float]:
    numOfVar = 2
    numOfConstraints = len(constraints)
    costs = np.array([*profit, *([0] * numOfConstraints)], dtype=float)

    tableau = np.zeros((numOfConstraints, numOfVar + numOfConstraints + 1), dtype=float)
    for rowIndex, (a1, a2, rhs, _) in enumerate(constraints):
        tableau[rowIndex, :2] = (a1, a2)
        tableau[rowIndex, numOfVar + rowIndex] = 1
        tableau[rowIndex, -1] = rhs

    basis = [numOfVar + i for i in range(numOfConstraints)]
    print("\n1) СИМПЛЕКС-МЕТОД")
    print("Начальная таблица:")
    printTableau(tableau, basis, costs)

    iteration = 0
    while True:
        zj = costs[basis] @ tableau[:, :-1]
        reducedCosts = costs - zj
        entering = int(np.argmax(reducedCosts))
        if reducedCosts[entering] <= 1e-9:
            break

        ratios = np.full(numOfConstraints, np.inf)
        positive = tableau[:, entering] > 1e-9
        ratios[positive] = tableau[positive, -1] / tableau[positive, entering]
        leaving = int(np.argmin(ratios))
        iteration += 1
        names = ["x1", "x2", "s1", "s2", "s3"]
        print(
            f"\nИтерация {iteration}: входит {names[entering]}, выходит {names[basis[leaving]]}; "
            f"опорное отношение = {formatNumber(ratios[leaving])}."
        )

        pivot = tableau[leaving][entering]
        tableau[leaving] /= pivot
        for i in range(numOfConstraints):
            if i == leaving:
                continue
            factor = tableau[i][entering]
            tableau[i] -= factor * tableau[leaving]
        basis[leaving] = entering
        printTableau(tableau, basis, costs)

    result = np.zeros(numOfVar)
    for row, basicVariable in zip(tableau, basis):
        if basicVariable < numOfVar:
            result[basicVariable] = row[-1]
    maximum = float(costs[basis] @ tableau[:, -1])
    print(
        f"\nОптимальный план: x1 = {formatNumber(result[0])}, x2 = {formatNumber(result[1])}"
    )
    print(f"Максимальная прибыль: Zmax = {formatNumber(maximum)} руб.")
    return result[0], result[1], maximum


def intersection(first: np.ndarray, second: np.ndarray) -> np.ndarray | None:
    matrix = np.array((first[:2], second[:2]), dtype=float)
    if np.isclose(np.linalg.det(matrix), 0):
        return None
    return np.linalg.solve(matrix, np.array((first[2], second[2]), dtype=float))


def graphicalMethod() -> tuple[float, float, float, np.ndarray]:
    boundaries = np.array(
        [
            *(constraint[:3] for constraint in constraints),
            (1, 0, 0),
            (0, 1, 0),
        ],
        dtype=float,
    )
    resourceMatrix = boundaries[:3, :2]
    resources = boundaries[:3, 2]

    vertices: list[np.ndarray] = []
    for i in range(len(boundaries)):
        for j in range(i + 1, len(boundaries)):
            point = intersection(boundaries[i], boundaries[j])
            if (
                point is not None
                and np.all(point >= -1e-9)
                and np.all(resourceMatrix @ point <= resources + 1e-9)
            ):
                if not any(np.allclose(point, existing) for existing in vertices):
                    vertices.append(point)

    orderedVertices = np.array(sorted(vertices, key=lambda point: (point[0], point[1])))
    values = orderedVertices @ np.array(profit)
    bestIndex = int(np.argmax(values))
    bestX1, bestX2 = orderedVertices[bestIndex]
    maximum = float(values[bestIndex])

    print("\n2) ГРАФИЧЕСКИЙ МЕТОД")
    print("Допустимые вершины:")
    for x1, x2 in orderedVertices:
        value = float(
            np.dot(np.array(profit, dtype=float), np.array((x1, x2), dtype=float))
        )
        print(f"({formatNumber(x1)}, {formatNumber(x2)}): Z = {formatNumber(value)}")
    print(f"\nЛучшая вершина: ({formatNumber(bestX1)}, {formatNumber(bestX2)})")
    print(f"Максимальная прибыль: Zmax = {formatNumber(maximum)} руб.")
    return bestX1, bestX2, maximum, orderedVertices


def savePlot(vertices: np.ndarray, optimum: tuple[float, float]) -> str:
    center = np.mean(vertices, axis=0)
    angles = np.arctan2(vertices[:, 1] - center[1], vertices[:, 0] - center[0])
    points = vertices[np.argsort(angles)]

    figure, axis = plt.subplots(figsize=(8, 6))
    xs = np.arange(0, 151)
    _ = axis.plot(xs, [(600 - 4 * x) / 5 for x in xs], label=r"$4x_1+5x_2=600$")
    _ = axis.plot(xs, [(540 - 6 * x) / 3 for x in xs], label=r"$6x_1+3x_2=540$")
    axis.axvline(60, label=r"$2x_1=120$")
    _ = axis.fill(
        points[:, 0],
        points[:, 1],
        color="tab:green",
        alpha=0.25,
        label="Допустимая область",
    )
    _ = axis.scatter(points[:, 0], points[:, 1], color="tab:green", zorder=3)
    _ = axis.scatter(*optimum, color="red", zorder=4, label="Оптимум (50, 80)")
    coefficient_vector = 5 * np.array(profit, dtype=float)
    _ = axis.quiver(
        0,
        0,
        coefficient_vector[0],
        coefficient_vector[1],
        angles="xy",
        scale_units="xy",
        scale=1,
        color="purple",
        width=0.006,
        zorder=5,
    )
    _ = axis.text(
        coefficient_vector[0] + 2,
        coefficient_vector[1] + 2,
        r"$\vec{c}=(6,7)$",
        color="purple",
    )
    _ = axis.set(
        xlim=(0, 150),
        ylim=(0, 185),
        xlabel=r"$x_1$ — изделия A",
        ylabel=r"$x_2$ — изделия B",
    )
    axis.grid(True, alpha=0.3)
    _ = axis.legend()
    figure.tight_layout()

    output_path = "variant6Graph.png"
    figure.savefig(output_path, dpi=160)
    plt.close(figure)
    return output_path


def main() -> None:
    print("Вариант 6. Задание 1")
    print("max Z = 6x1 + 7x2")
    print("Ограничения: 4x1 + 5x2 <= 600; 6x1 + 3x2 <= 540; 2x1 <= 120.")

    simplex_x1, simplex_x2, simplex_value = simplexMethod()
    graph_x1, graph_x2, graph_value, vertices = graphicalMethod()
    assert np.allclose(
        (simplex_x1, simplex_x2, simplex_value),
        (graph_x1, graph_x2, graph_value),
    )

    chart = savePlot(vertices, (graph_x1, graph_x2))
    print(f"\nГрафик сохранён: {chart}")


if __name__ == "__main__":
    main()
