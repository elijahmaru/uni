graph = {
    "Arad": {"Zerind": 75, "Sibiu": 140, "Timisoara": 118},
    "Zerind": {"Arad": 75, "Oradea": 71},
    "Oradea": {"Zerind": 71, "Sibiu": 151},
    "Sibiu": {"Arad": 140, "Oradea": 151, "Fagaras": 99, "Rimnicu Vilcea": 80},
    "Timisoara": {"Arad": 118, "Lugoj": 111},
    "Lugoj": {"Timisoara": 111, "Mehadia": 70},
    "Mehadia": {"Lugoj": 70, "Drobeta": 75},
    "Drobeta": {"Mehadia": 75, "Craiova": 120},
    "Craiova": {"Drobeta": 120, "Rimnicu Vilcea": 146, "Pitesti": 138},
    "Rimnicu Vilcea": {"Sibiu": 80, "Craiova": 146, "Pitesti": 97},
    "Fagaras": {"Sibiu": 99, "Bucuresti": 211},
    "Pitesti": {"Rimnicu Vilcea": 97, "Craiova": 138, "Bucuresti": 101},
    "Bucuresti": {"Fagaras": 211, "Pitesti": 101, "Giurgiu": 90, "Urziceni": 85},
    "Giurgiu": {"Bucuresti": 90},
    "Urziceni": {"Bucuresti": 85, "Hirsova": 98, "Vaslui": 142},
    "Hirsova": {"Urziceni": 98, "Eforie": 86},
    "Eforie": {"Hirsova": 86},
    "Vaslui": {"Urziceni": 142, "Iasi": 92},
    "Iasi": {"Vaslui": 92, "Neamt": 87},
    "Neamt": {"Iasi": 87},
}
heuristics = {
    "Arad": 366,
    "Bucuresti": 0,
    "Craiova": 160,
    "Drobeta": 242,
    "Eforie": 161,
    "Fagaras": 176,
    "Giurgiu": 77,
    "Hirsova": 151,
    "Iasi": 226,
    "Lugoj": 244,
    "Mehadia": 241,
    "Neamt": 234,
    "Oradea": 380,
    "Pitesti": 100,
    "Rimnicu Vilcea": 193,
    "Sibiu": 253,
    "Timisoara": 329,
    "Urziceni": 80,
    "Vaslui": 199,
    "Zerind": 374,
}


def broadFirstSearch():
    queue = [["Arad", ["Arad"], 0]]
    visited = set()
    nodeUsed = 0

    while queue:
        node, path, cost = queue.pop(0)
        nodeUsed += 1
        if node == "Bucuresti":
            return path, cost, nodeUsed
        if node not in visited:
            visited.add(node)
            for neighbor, toNeighbor in graph[node].items():
                if neighbor not in visited:
                    queue.append(
                        [neighbor, path + [neighbor], cost + toNeighbor])
    return None


def deapthFirstSearch():
    queue = [["Arad", ["Arad"], 0]]
    visited = set()
    nodeUsed = 0

    while queue:
        node, path, cost = queue.pop()
        nodeUsed += 1
        if node == "Bucuresti":
            return path, cost, nodeUsed
        if node not in visited:
            visited.add(node)
            for neighbor, toNeighbor in graph[node].items():
                if neighbor not in visited:
                    queue.append(
                        [neighbor, path + [neighbor], cost + toNeighbor])


def unifromCostSearch():
    queue = [["Arad", ["Arad"], 0]]
    visited = set()
    nodeUsed = 0

    while queue:
        queue.sort(key=lambda x: x[2])
        node, path, cost = queue.pop(0)
        nodeUsed += 1
        if node == "Bucuresti":
            return path, cost, nodeUsed
        if node not in visited:
            visited.add(node)
            for neighbor, toNeighbor in graph[node].items():
                if neighbor not in visited:
                    queue.append(
                        [neighbor, path + [neighbor], cost + toNeighbor])


def greedyBestFirstSearch():
    queue = [[heuristics["Arad"], "Arad", ["Arad"], 0]]
    visisted = set()
    nodeUsed = 0

    while queue:
        queue.sort(key=lambda x: x[0])
        weight, node, path, cost = queue.pop()
        nodeUsed += 1
        if node == "Bucuresti":
            return path, cost, nodeUsed
        if node not in visisted:
            visisted.add(node)
            for neighbor, toNeighbor in graph[node].items():
                if neighbor not in visisted:
                    queue.append(
                        [
                            heuristics[node],
                            neighbor,
                            path + [neighbor],
                            cost + toNeighbor,
                        ]
                    )


print("BFS: ", " => ".join(broadFirstSearch()[0]), broadFirstSearch()[1:])
print("DFS: ", " => ".join(deapthFirstSearch()[0]), deapthFirstSearch()[1:])
print("UCS: ", " => ".join(unifromCostSearch()[0]), unifromCostSearch()[1:])
print("GBFS: ", " => ".join(greedyBestFirstSearch()[0]), greedyBestFirstSearch()[1:])
