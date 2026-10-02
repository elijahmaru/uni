"""Лабораторная работа 2 — вариант 6, задание 1.

Решение ЗЛП двумя способами:
1. симплекс-методом;
2. графическим методом (по всем вершинам допустимой области).
"""

import matplotlib.pyplot as plt
import numpy as np


# Данные варианта 6 из таблицы задания.
# x1 — число изделий A, x2 — число изделий B.
CONSTRAINTS = (
    (4, 5, 600, "Сырьё 1"),
    (6, 3, 540, "Сырьё 2"),
    (2, 0, 120, "Сырьё 3"),
)
PROFIT = (6, 7)


def format_number(value: float) -> str:
    """Красиво выводит целые числа и десятичные значения."""
    return str(int(round(value))) if np.isclose(value, round(value)) else f"{value:.2f}"


def print_tableau(tableau: np.ndarray, basis: list[int], costs: np.ndarray) -> None:
    """Печатает текущую симплекс-таблицу и строку Cj - Zj."""
    variable_names = ["x1", "x2", "s1", "s2", "s3"]
    header = ["Базис", "Cb", "b", *variable_names]
    rows: list[list[str]] = []

    for row, basic_variable in zip(tableau, basis):
        rows.append(
            [
                variable_names[basic_variable],
                format_number(costs[basic_variable]),
                format_number(row[-1]),
                *(format_number(value) for value in row[:-1]),
            ]
        )

    zj = costs[basis] @ tableau[:, :-1]
    reduced_costs = costs - zj
    rows.append(["Cj − Zj", "", "", *(format_number(value) for value in reduced_costs)])

    widths = [max(len(header[i]), *(len(row[i]) for row in rows)) for i in range(len(header))]
    print("  ".join(title.rjust(widths[i]) for i, title in enumerate(header)))
    for row in rows:
        print("  ".join(cell.rjust(widths[i]) for i, cell in enumerate(row)))


def simplex_method() -> tuple[float, float, float]:
    """Находит максимум симплекс-методом для задачи max с ограничениями <=."""
    n_variables = 2
    n_constraints = len(CONSTRAINTS)
    costs = np.array([*PROFIT, *([0] * n_constraints)], dtype=float)

    # [коэффициенты x1, x2, s1, s2, s3, свободный член]
    tableau = np.zeros((n_constraints, n_variables + n_constraints + 1), dtype=float)
    for row_index, (a1, a2, rhs, _) in enumerate(CONSTRAINTS):
        tableau[row_index, :2] = (a1, a2)
        tableau[row_index, n_variables + row_index] = 1
        tableau[row_index, -1] = rhs

    basis = [n_variables + i for i in range(n_constraints)]
    print("\n1) СИМПЛЕКС-МЕТОД")
    print("Начальная таблица:")
    print_tableau(tableau, basis, costs)

    iteration = 0
    while True:
        zj = costs[basis] @ tableau[:, :-1]
        reduced_costs = costs - zj
        entering = int(np.argmax(reduced_costs))
        if reduced_costs[entering] <= 1e-9:
            break

        ratios = np.full(n_constraints, np.inf)
        positive = tableau[:, entering] > 1e-9
        ratios[positive] = tableau[positive, -1] / tableau[positive, entering]
        leaving = int(np.argmin(ratios))
        iteration += 1
        names = ["x1", "x2", "s1", "s2", "s3"]
        print(
            f"\nИтерация {iteration}: входит {names[entering]}, выходит {names[basis[leaving]]}; "
            f"опорное отношение = {format_number(ratios[leaving])}."
        )

        pivot = tableau[leaving][entering]
        tableau[leaving] /= pivot
        for i in range(n_constraints):
            if i == leaving:
                continue
            factor = tableau[i][entering]
            tableau[i] -= factor * tableau[leaving]
        basis[leaving] = entering
        print_tableau(tableau, basis, costs)

    result = np.zeros(n_variables)
    for row, basic_variable in zip(tableau, basis):
        if basic_variable < n_variables:
            result[basic_variable] = row[-1]
    maximum = float(costs[basis] @ tableau[:, -1])
    print(f"\nОптимальный план: x1 = {format_number(result[0])}, x2 = {format_number(result[1])}")
    print(f"Максимальная прибыль: Zmax = {format_number(maximum)} руб.")
    return result[0], result[1], maximum


def intersection(first: np.ndarray, second: np.ndarray) -> np.ndarray | None:
    """Возвращает пересечение двух прямых ax + by = c."""
    matrix = np.array((first[:2], second[:2]), dtype=float)
    if np.isclose(np.linalg.det(matrix), 0):
        return None
    return np.linalg.solve(matrix, np.array((first[2], second[2]), dtype=float))


def graphical_method() -> tuple[float, float, float, np.ndarray]:
    """Находит все допустимые вершины и выбирает вершину с наибольшей прибылью."""
    # Добавляем границы неотрицательности x1 = 0 и x2 = 0.
    boundaries = np.array(
        [
            *(constraint[:3] for constraint in CONSTRAINTS),
            (1, 0, 0),
            (0, 1, 0),
        ],
        dtype=float,
    )
    resource_matrix = boundaries[:3, :2]
    resources = boundaries[:3, 2]

    vertices: list[np.ndarray] = []
    for i in range(len(boundaries)):
        for j in range(i + 1, len(boundaries)):
            point = intersection(boundaries[i], boundaries[j])
            if point is not None and np.all(point >= -1e-9) and np.all(resource_matrix @ point <= resources + 1e-9):
                if not any(np.allclose(point, existing) for existing in vertices):
                    vertices.append(point)

    ordered_vertices = np.array(sorted(vertices, key=lambda point: (point[0], point[1])))
    values = ordered_vertices @ np.array(PROFIT)
    best_index = int(np.argmax(values))
    best_x1, best_x2 = ordered_vertices[best_index]
    maximum = float(values[best_index])

    print("\n2) ГРАФИЧЕСКИЙ МЕТОД")
    print("Допустимые вершины:")
    for x1, x2 in ordered_vertices:
        value = float(np.dot(np.array(PROFIT, dtype=float), np.array((x1, x2), dtype=float)))
        print(f"({format_number(x1)}, {format_number(x2)}): Z = {format_number(value)}")
    print(f"\nЛучшая вершина: ({format_number(best_x1)}, {format_number(best_x2)})")
    print(f"Максимальная прибыль: Zmax = {format_number(maximum)} руб.")
    return best_x1, best_x2, maximum, ordered_vertices


def save_plot(vertices: np.ndarray, optimum: tuple[float, float]) -> str:
    """Строит область допустимых решений для графического метода."""
    center = np.mean(vertices, axis=0)
    angles = np.arctan2(vertices[:, 1] - center[1], vertices[:, 0] - center[0])
    points = vertices[np.argsort(angles)]

    figure, axis = plt.subplots(figsize=(8, 6))
    xs = np.arange(0, 151)
    axis.plot(xs, [(600 - 4 * x) / 5 for x in xs], label=r"$4x_1+5x_2=600$")
    axis.plot(xs, [(540 - 6 * x) / 3 for x in xs], label=r"$6x_1+3x_2=540$")
    axis.axvline(60, label=r"$2x_1=120$")
    axis.fill(points[:, 0], points[:, 1], color="tab:green", alpha=0.25, label="Допустимая область")
    axis.scatter(points[:, 0], points[:, 1], color="tab:green", zorder=3)
    axis.scatter(*optimum, color="red", zorder=4, label="Оптимум (50, 80)")
    # Вектор коэффициентов целевой функции c = (6, 7).
    # Увеличен в 5 раз только для наглядности на графике.
    coefficient_vector = 5 * np.array(PROFIT, dtype=float)
    axis.quiver(
        0, 0, coefficient_vector[0], coefficient_vector[1],
        angles="xy", scale_units="xy", scale=1, color="purple", width=0.006, zorder=5,
    )
    axis.text(
        coefficient_vector[0] + 2,
        coefficient_vector[1] + 2,
        r"$\vec{c}=(6,7)$",
        color="purple",
    )
    axis.set(xlim=(0, 150), ylim=(0, 185), xlabel=r"$x_1$ — изделия A", ylabel=r"$x_2$ — изделия B")
    axis.grid(True, alpha=0.3)
    axis.legend()
    figure.tight_layout()

    output_path = "variant_6_graph.png"
    figure.savefig(output_path, dpi=160)
    plt.close(figure)
    return output_path


def main() -> None:
    print("Вариант 6. Задание 1")
    print("max Z = 6x1 + 7x2")
    print("Ограничения: 4x1 + 5x2 <= 600; 6x1 + 3x2 <= 540; 2x1 <= 120.")

    simplex_x1, simplex_x2, simplex_value = simplex_method()
    graph_x1, graph_x2, graph_value, vertices = graphical_method()
    assert np.allclose(
        (simplex_x1, simplex_x2, simplex_value),
        (graph_x1, graph_x2, graph_value),
    )

    chart = save_plot(vertices, (graph_x1, graph_x2))
    print(f"\nГрафик сохранён: {chart}")


if __name__ == "__main__":
    main()
