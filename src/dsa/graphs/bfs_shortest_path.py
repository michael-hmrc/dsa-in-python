from collections import deque

graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}

def bfs_shortest_path(start, target):

    queue = deque([(start, 0)])  # (node, distance)
    visited = {start}

    while queue:
        node, dist = queue.popleft()

        if node == target:
            return dist

        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                queue.append((nei, dist + 1))

    return -1

if __name__ == "__main__":
    print(bfs_shortest_path(0)) 
