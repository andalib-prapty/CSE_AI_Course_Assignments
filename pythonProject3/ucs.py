# Uniform Cost Search Algorithm
graph = {
    'A': {'B': 3, 'C': 2, 'D': 1},
    'B': {'A': 3, 'E': 5},
    'C': {'A': 2, 'G': 4},
    'D': {'A': 1, 'F': 2},
    'E': {'B': 5, 'G': 4},
    'F': {'D': 2, 'G': 8},
    'G': {'C': 4, 'E': 4, 'F': 8}
}

def ucs(graph, start, goal):
    queue = [(0, [start])]
    visited = {}

    while queue:
        queue.sort(key=lambda x: x[0])
        cost, path = queue.pop(0)
        node = path[-1]


        if node == goal:
            return path, cost


        if node not in visited or cost < visited[node]:
            visited[node] = cost


            for neighbor, edge_cost in graph[node].items():
                new_cost = cost + edge_cost
                new_path = path + [neighbor]
                queue.append((new_cost, new_path))

    return None, None


# Run the algorithm


path, cost = ucs(graph, 'A', 'G')

print("Path:", " -> ".join(path))
print("Total Cost:", cost)
