# Step 1: Represent the graph as an adjacency list
graph = {
    'A': ['E', 'B', 'C'],
    'B': ['A', 'D', 'G'],
    'C': ['A', 'G', 'E'],
    'D': ['B', 'H'],
    'E': ['A', 'C'],
    'G': ['B', 'C'],
    'H': ['D']
}


# Step 2: Define DFS-based cycle detection
def dfs_cycle(graph, node, visited, parent):
    visited[node] = True

    for neighbor in graph[node]:
        if not visited.get(neighbor, False):
            if dfs_cycle(graph, neighbor, visited, node):
                return True
        elif parent != neighbor:
            # Found a visited node that is not parent → cycle exists
            return True
    return False


# Step 3: Check all components
def has_cycle(graph):
    visited = {}
    for node in graph:
        if not visited.get(node, False):
            if dfs_cycle(graph, node, visited, None):
                return True
    return False


# Step 4: Run
if has_cycle(graph):
    print("Cycle detected in the graph.")
else:
    print("No cycle in the graph.")

