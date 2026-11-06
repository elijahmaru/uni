import yaml

with open("input.yaml", "r") as input:
    data = yaml.safe_load(input) or {}

amountOfOrigins = len(data["origins"])
amountOfDestinations = len(data["destinations"])

dictOfPrices = data["costs"]
costs = []
costs += [[0] * amountOfDestinations for _ in range(amountOfOrigins)]

for key in dictOfPrices.keys():
    row, column = (int(x) - 1 for x in list(key)[1:])
    costs[row][column] = dictOfPrices[key]

supplies = [0 for _ in range(amountOfOrigins)]
for supplyKey in data["supply"].keys():
    supplier = int(list(supplyKey)[-1]) - 1
    supplies[supplier] = data["supply"][supplyKey]

demands = [0 for _ in range(amountOfDestinations)]
for demandKey in data["demand"].keys():
    reciver = int(list(demandKey)[-1]) - 1
    demands[reciver] = data["demand"][demandKey]


def transportationCost(plan, costs):
    return sum(
        plan[i][j] * costs[i][j] for i in range(len(plan)) for j in range(len(plan[0]))
    )


def printPlan(name, plan, costs):
    print(f"\n{name}")
    for row in plan:
        print(*row)
    print("Стоимость:", transportationCost(plan, costs))


def northWestCorner(supplies, demands):
    supply = supplies.copy()
    demand = demands.copy()

    m = len(supply)
    n = len(demand)
    plan = [[0] * n for _ in range(m)]

    i = j = 0

    while i < m and j < n:
        amount = min(supply[i], demand[j])

        plan[i][j] = amount
        supply[i] -= amount
        demand[j] -= amount

        if supply[i] == 0:
            i += 1
        elif demand[j] == 0:
            j += 1

    return plan


def minimumCostMethod(costs, supplies, demands):
    supply = supplies.copy()
    demand = demands.copy()

    m = len(supply)
    n = len(demand)
    plan = [[0] * n for _ in range(m)]

    active_rows = set(range(m))
    active_cols = set(range(n))

    while active_rows and active_cols:
        i, j = min(
            ((i, j) for i in active_rows for j in active_cols),
            key=lambda cell: costs[cell[0]][cell[1]],
        )

        amount = min(supply[i], demand[j])

        plan[i][j] += amount
        supply[i] -= amount
        demand[j] -= amount

        if supply[i] == 0:
            active_rows.remove(i)

        if demand[j] == 0:
            active_cols.remove(j)

    return plan



def vogelMethod(costs, supplies, demands):
    supply = supplies.copy()
    demand = demands.copy()

    m = len(supply)
    n = len(demand)

    plan = [[0] * n for _ in range(m)]

    activeRows = set(range(m))
    activeCols = set(range(n))

    while activeRows and activeCols:
        candidates = []

        for i in activeRows:
            values = sorted((costs[i][j], j) for j in activeCols)

            if len(values) >= 2:
                penalty = values[1][0] - values[0][0]
            else:
                penalty = values[0][0]

            minCost, min_j = values[0]

            candidates.append((penalty, -minCost, "row", i, min_j))

        for j in activeCols:
            values = sorted((costs[i][j], i) for i in activeRows)

            if len(values) >= 2:
                penalty = values[1][0] - values[0][0]
            else:
                penalty = values[0][0]

            minCost, minI = values[0]

            candidates.append((penalty, -minCost, "column", j, minI))

        _, _, kind, index, second_index = max(candidates)

        if kind == "row":
            i = index
            j = second_index
        else:
            j = index
            i = second_index

        amount = min(supply[i], demand[j])

        plan[i][j] += amount
        supply[i] -= amount
        demand[j] -= amount

        if supply[i] == 0:
            activeRows.remove(i)

        if demand[j] == 0:
            activeCols.remove(j)
    return plan

def doublePriorityMethod(costs, supplies, demands):
    supply = supplies.copy()
    demand = demands.copy()

    m = len(supply)
    n = len(demand)

    plan = [[0] * n for _ in range(m)]

    priorities = [[0] * n for _ in range(m)]

    for i in range(m):
        minCost = min(costs[i])

        for j in range(n):
            if costs[i][j] == minCost:
                priorities[i][j] += 1

    for j in range(n):
        minCost = min(costs[i][j] for i in range(m))

        for i in range(m):
            if costs[i][j] == minCost:
                priorities[i][j] += 1

    activeRows = set(range(m))
    activeCols = set(range(n))

    while activeRows and activeCols:

        i, j = min(
            (
                (i, j)
                for i in activeRows
                for j in activeCols
            ),
            key=lambda cell: (
                -priorities[cell[0]][cell[1]],
                costs[cell[0]][cell[1]],
                cell[0],
                cell[1]
            )
        )

        amount = min(supply[i], demand[j])

        plan[i][j] += amount

        supply[i] -= amount
        demand[j] -= amount

        if supply[i] == 0:
            activeRows.remove(i)

        if demand[j] == 0:
            activeCols.remove(j)

    return plan

def getBasis(plan):
    return {
        (i, j)
        for i in range(len(plan))
        for j in range(len(plan[0]))
        if plan[i][j] > 0
    }


def makeNondegenerateBasis(plan):
    m = len(plan)
    n = len(plan[0])

    basis = getBasis(plan)

    parent = list(range(m + n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra = find(a)
        rb = find(b)

        if ra == rb:
            return False

        parent[rb] = ra
        return True

    for i, j in basis:
        union(i, m + j)

    for i in range(m):
        for j in range(n):
            if len(basis) == m + n - 1:
                return basis

            if (i, j) not in basis:
                if union(i, m + j):
                    basis.add((i, j))

    return basis



def calculatePotentials(costs, basis):
    m = len(costs)
    n = len(costs[0])

    u = [None] * m
    v = [None] * n

    u[0] = 0

    changed = True

    while changed:
        changed = False

        for i, j in basis:
            if u[i] is not None and v[j] is None:
                v[j] = costs[i][j] - u[i]
                changed = True

            elif v[j] is not None and u[i] is None:
                u[i] = costs[i][j] - v[j]
                changed = True

    if any(x is None for x in u + v):
        raise RuntimeError(
            "Не удалось вычислить потенциалы: "
            "базис не является связным."
        )

    return u, v

def calculateDeltas(costs, u, v, basis):
    m = len(costs)
    n = len(costs[0])

    deltas = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if (i, j) not in basis:
                deltas[i][j] = (
                    costs[i][j] - u[i] - v[j]
                )

    return deltas


def printDeltas(deltas):
    print("\nОценки небазисных клеток Δ:")

    for row in deltas:
        for value in row:
            if value is None:
                print("   -", end=" ")
            else:
                print(f"{value:4}", end=" ")

        print()


def findCycle(basis, enteringCell):
    start = enteringCell

    cells = set(basis)
    cells.add(start)

    def dfs(path, moveByRow):
        current = path[-1]
        i, j = current

        candidates = []

        if moveByRow:
            for cell in cells:
                if (
                    cell != current
                    and cell[0] == i
                    and cell not in path[1:]
                ):
                    candidates.append(cell)
        else:
            for cell in cells:
                if (
                    cell != current
                    and cell[1] == j
                    and cell not in path[1:]
                ):
                    candidates.append(cell)

        for nextCell in candidates:

            if nextCell == start and len(path) >= 4:
                return path

            if nextCell in path:
                continue

            result = dfs(
                path + [nextCell],
                not moveByRow
            )

            if result is not None:
                return result

        return None

    cycle = dfs([start], True)

    if cycle is None:
        cycle = dfs([start], False)

    return cycle


def optimizeTransportationPlan(costs, initialPlan):
    plan = [row.copy() for row in initialPlan]

    iteration = 1

    while True:
        print("\n" + "=" * 60)
        print(f"ИТЕРАЦИЯ {iteration}")
        print("=" * 60)

        print("\nТекущий план:")

        for row in plan:
            print(*row)

        current_cost = transportationCost(plan, costs)

        print("\nТекущая стоимость:", current_cost)
        basis = makeNondegenerateBasis(plan)

        print("\nБазисные клетки:")

        for i, j in sorted(basis):
            print(
                f"A{i + 1} -> B{j + 1}, "
                f"x = {plan[i][j]}"
            )
        u, v = calculatePotentials(
            costs,
            basis
        )

        print("\nПотенциалы:")
        print("u =", u)
        print("v =", v)


        deltas = calculateDeltas(
            costs,
            u,
            v,
            basis
        )

        printDeltas(deltas)

        negativeCells = []

        for i in range(len(costs)):
            for j in range(len(costs[0])):

                if (
                    deltas[i][j] is not None
                    and deltas[i][j] < 0
                ):
                    negativeCells.append(
                        (deltas[i][j], i, j)
                    )

        if not negativeCells:
            print("\nВсе оценки Δ >= 0.")
            print("План ОПТИМАЛЕН.")

            print(
                "\nМинимальная стоимость:",
                transportationCost(plan, costs)
            )

            return plan


        delta, enterI, enterJ = min(
            negativeCells
        )

        enteringCell = (enterI, enterJ)

        print(
            "\nНаиболее отрицательная оценка:"
        )

        print(
            f"Δ[{enterI + 1}][{enterJ + 1}] "
            f"= {delta}"
        )

        print(
            f"В базис входит клетка "
            f"A{enterI + 1} -> B{enterJ + 1}"
        )

        cycle = findCycle(
            basis,
            enteringCell
        )

        if cycle is None:
            raise RuntimeError(
                "Не удалось построить цикл."
            )

        print("\nЦикл перераспределения:")

        for k, (i, j) in enumerate(cycle):
            sign = "+" if k % 2 == 0 else "-"

            print(
                f"{sign} "
                f"A{i + 1} -> B{j + 1}"
            )


        minusCells = cycle[1::2]

        theta = min(
            plan[i][j]
            for i, j in minusCells
        )

        print("\ntheta =", theta)


        for k, (i, j) in enumerate(cycle):

            if k % 2 == 0:
                plan[i][j] += theta
            else:
                plan[i][j] -= theta

        print(
            "\nСтоимость после перераспределения:",
            transportationCost(plan, costs)
        )

        iteration += 1



northWestPlan = northWestCorner(
    supplies,
    demands
)

minCostPlan = minimumCostMethod(
    costs,
    supplies,
    demands
)

vogelPlan = vogelMethod(
    costs,
    supplies,
    demands
)

doublePriorityPlan = doublePriorityMethod(
    costs,
    supplies,
    demands
)

printPlan(
    "1. Метод северо-западного угла",
    northWestPlan,
    costs
)

printPlan(
    "2. Метод минимальной стоимости",
    minCostPlan,
    costs
)

printPlan(
    "3. Метод Фогеля",
    vogelPlan,
    costs
)

printPlan(
    "4. Метод двойного предпочтения",
    doublePriorityPlan,
    costs
)

plans = {
    "Северо-западный угол": northWestPlan,
    "Минимальная стоимость": minCostPlan,
    "Метод Фогеля": vogelPlan,
    "Двойное предпочтение": doublePriorityPlan
}

bestName, bestPlan = min(
    plans.items(),
    key=lambda item: transportationCost(
        item[1],
        costs
    )
)

print("\n" + "=" * 60)
print("ЛУЧШИЙ НАЧАЛЬНЫЙ ПЛАН")
print("=" * 60)

print("Метод:", bestName)

for row in bestPlan:
    print(*row)

print(
    "Стоимость:",
    transportationCost(bestPlan, costs)
)



optimal_plan = optimizeTransportationPlan(
    costs,
    bestPlan
)



print("\n" + "=" * 60)
print("ОПТИМАЛЬНЫЙ ПЛАН")
print("=" * 60)

for row in optimal_plan:
    print(*row)

print(
    "\nМинимальная стоимость:",
    transportationCost(
        optimal_plan,
        costs
    )
)

