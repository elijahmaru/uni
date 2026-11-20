import heapq
import math

INF = math.inf

cost = [
    [INF, 31, 15, 19, 8, 55],
    [19, INF, 22, 31, 7, 35],
    [25, 43, INF, 53, 57, 16],
    [5, 50, 49, INF, 39, 9],
    [24, 24, 33, 5, INF, 14],
    [34, 26, 6, 3, 36, INF],
]


def tsp_branch_and_bound_matrix(cost, start=0):
    n = len(cost)
    if n < 2 or any(len(row) != n for row in cost):
        raise ValueError(
            "Ожидается квадратная матрица стоимости минимум для двух городов."
        )

    all_visited = (1 << n) - 1
    step = 0

    def route_text(path):
        return " -> ".join(str(city + 1) for city in path)

    def remaining_matrix(current, visited):
        unvisited = [v for v in range(n) if not visited & (1 << v)]
        sources = [current] + unvisited
        targets = unvisited + [start]
        matrix = [[INF] * n for _ in range(n)]

        for u in sources:
            for v in targets:
                if u == v:
                    continue
                if u == current and v == start and unvisited:
                    continue
                matrix[u][v] = cost[u][v]

        return matrix, sources, targets

    def show_matrix(label, current, visited, current_cost, path, best_cost=None):
        nonlocal step
        step += 1
        matrix, sources, targets = remaining_matrix(current, visited)

        row_mins = {u: min(matrix[u][v] for v in targets) for u in sources}
        col_mins = {v: min(matrix[u][v] for u in sources) for v in targets}

        outgoing = sum(row_mins.values())
        incoming = sum(col_mins.values())
        bound = current_cost + max(outgoing, incoming)

        print(f"\n{'=' * 63}")
        print(f"ШАГ МАТРИЦЫ {step}: {label}")
        print(f"Путь: {route_text(path)}   |   Текущая стоимость: {current_cost}")
        print(
            "'--' = недоступное ребро; справа и снизу показаны минимумы строк и столбцов"
        )
        print(
            f"{'Из/В':>9}" + "".join(f"{v + 1:>7}" for v in range(n)) + " | Мин. строки"
        )
        print("-" * (11 + 7 * n + 11))

        for u in range(n):
            cells = "".join(
                f"{('--' if matrix[u][v] == INF else str(matrix[u][v])):>7}"
                for v in range(n)
            )
            row_min = (
                "--" if u not in row_mins or row_mins[u] == INF else str(row_mins[u])
            )
            print(f"{u + 1:>9}{cells} | {row_min:>7}")

        mins = "".join(
            f"{('--' if v not in col_mins or col_mins[v] == INF else str(col_mins[v])):>7}"
            for v in range(n)
        )
        print("-" * (11 + 7 * n + 11))
        print(f"{'Мин. ст.':>9}{mins}")
        print(f"Сумма минимумов по строкам: {outgoing}")
        print(f"Сумма минимумов по столбцам: {incoming}")
        print(
            f"Нижняя оценка = {current_cost} + макс({outgoing}, {incoming}) = {bound}"
        )
        if best_cost is not None:
            print(f"Лучшая стоимость полного маршрута: {best_cost}")
        return bound

    # Начальная матрица.
    start_mask = 1 << start
    show_matrix("Начальное состояние", start, start_mask, 0, (start,))

    current = start
    visited = start_mask
    greedy_path = (start,)
    greedy_cost = 0

    while visited != all_visited:
        next_city = min(
            (v for v in range(n) if not (visited & (1 << v))),
            key=lambda v: (cost[current][v], v),
        )
        greedy_cost += cost[current][next_city]
        current = next_city
        visited |= 1 << next_city
        greedy_path += (next_city,)
        show_matrix(
            f"Жадный алгоритм выбрал город {current + 1}",
            current,
            visited,
            greedy_cost,
            greedy_path,
        )

    greedy_cost += cost[current][start]
    best_cost = greedy_cost
    best_route = greedy_path + (start,)
    print(
        f"\nПолный маршрут жадного алгоритма: {route_text(best_route)} | Стоимость: {best_cost}"
    )

    # Метод ветвей и границ с очередью по оценке и отсечением одинаковых состояний.
    first_bound = show_matrix(
        "Корневая ветвь", start, start_mask, 0, (start,), best_cost
    )
    queue = [(first_bound, 0, start, start_mask, (start,))]
    best_state_cost = {(start_mask, start): 0}
    iteration = 0

    while queue:
        bound, current_cost, current, visited, path = heapq.heappop(queue)
        iteration += 1
        print(
            f"\n>>> ИТЕРАЦИЯ №{iteration}: {route_text(path)} | оценка из очереди = {bound}"
        )

        # Более дорогой путь к уже найденному состоянию может устареть.
        if current_cost > best_state_cost.get((visited, current), INF):
            show_matrix(
                "Устаревшее состояние", current, visited, current_cost, path, best_cost
            )
            print("ОТСЕЧЕНО: для такого же состояния найден более дешёвый путь.")
            continue

        shown_bound = show_matrix(
            "Рассматриваем текущую ветвь",
            current,
            visited,
            current_cost,
            path,
            best_cost,
        )
        assert shown_bound == bound

        if bound >= best_cost:
            print("ОТСЕЧЕНО: нижняя оценка не меньше стоимости лучшего маршрута.")
            continue

        if visited == all_visited:
            total = current_cost + cost[current][start]
            full_path = path + (start,)
            print(f"ПОЛНЫЙ МАРШРУТ: {route_text(full_path)} | Стоимость: {total}")
            if total < best_cost:
                best_cost = total
                best_route = full_path
                print("НАЙДЕН НОВЫЙ ЛУЧШИЙ МАРШРУТ!")
            continue

        for next_city in range(n):
            if visited & (1 << next_city):
                continue
            if cost[current][next_city] == INF:
                continue

            new_cost = current_cost + cost[current][next_city]
            new_path = path + (next_city,)
            new_visited = visited | (1 << next_city)
            state = (new_visited, next_city)

            new_bound = show_matrix(
                f"Пробуем переход {current + 1} -> {next_city + 1}",
                next_city,
                new_visited,
                new_cost,
                new_path,
                best_cost,
            )

            if new_cost >= best_cost:
                print("ОТСЕЧЕНО: стоимость частичного пути уже не меньше лучшей.")
            elif new_cost >= best_state_cost.get(state, INF):
                print(
                    "ОТСЕЧЕНО: те же посещённые города и конечный город уже достигнуты дешевле."
                )
            elif new_bound >= best_cost:
                print("ОТСЕЧЕНО: нижняя оценка по матрице слишком велика.")
            else:
                best_state_cost[state] = new_cost
                heapq.heappush(
                    queue,
                    (new_bound, new_cost, next_city, new_visited, new_path),
                )
                print("СОХРАНЕНО: состояние добавлено в очередь с приоритетом.")

    print("\n" + "=" * 63)
    print("ОПТИМАЛЬНЫЙ МАРШРУТ:", route_text(best_route))
    print("МИНИМАЛЬНАЯ СТОИМОСТЬ:", best_cost)
    return best_cost, best_route


if __name__ == "__main__":
    tsp_branch_and_bound_matrix(cost)
