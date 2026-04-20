graph = {
    'A': {'B': 3, 'C': 2, 'D': 1},
    'B': {'A': 3, 'E': 5},
    'C': {'A': 2, 'G': 4},
    'D': {'A': 1, 'F': 2},
    'E': {'B': 5, 'G': 4},
    'F': {'D': 2, 'G': 8},
    'G': {'C': 4, 'E': 4, 'F': 8}
}

#from nodes to G
heuristic = {
    'A': 5,
    'B': 7,
    'C': 1,
    'D': 4,
    'E': 1,
    'F': 2,
    'G': 0
}

def a_star(graph, start, goal, heuristic):
    queue = [(start, 0 + heuristic[start], 0, [start])]
    visited = set()

    while queue:
        queue.sort(key=lambda x: x[1])
        node, f, g, path = queue.pop(0)

        if node == goal:
            return path, g

        visited.add(node)

        for neighbor, cost in graph[node].items():
            if neighbor not in visited:
                g_new = g + cost
                f_new = g_new + heuristic[neighbor]
                queue.append((neighbor, f_new, g_new, path + [neighbor]))

    return None, None

path, cost = a_star(graph, 'A', 'G', heuristic)
print("\nPath:", " → ".join(path))
print("Total Cost:", cost)