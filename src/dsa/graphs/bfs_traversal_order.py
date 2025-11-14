# BFS helps with:

# shortest path in unweighted graph

# level order traversal

# Template:

from collections import deque


def bfs_traversal_order(start, graph):
    queue = deque([start])
    visited = set([start])
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)

    return order                        


if __name__ == "__main__":
    
    num_graph = {
        0: [1, 3],
        1: [0, 2],
        2: [1, 3],
        3: [0, 2]
    }

    alpha_graph = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["B", "C"]
    }
    
    print(bfs_traversal_order(0), num_graph) 
    print(bfs_traversal_order("A", alpha_graph)) 
