# BFS helps with:

# shortest path in unweighted graph

# level order traversal

# Template:


graph = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}

from collections import deque


def bfs(start):
    queue = deque([start])
    visited = set([start])

    while queue:
        node = queue.popleft()
        print(node)

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append(nei)


if __name__ == "__main__":
    print(bfs(0))
