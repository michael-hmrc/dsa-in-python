from collections import deque

def bfs_level_order(start, graph):
    queue = deque([start])
    visited = {start}
    levels = []

    while queue:
        size = len(queue)
        level = []

        for _ in range(size):
            node = queue.popleft()
            level.append(node)

            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    queue.append(nei)

        levels.append(level)

    return levels

if __name__ == "__main__":
    
    graph = {
        0: [1, 3],
        1: [0, 2],
        2: [1, 3],
        3: [0, 2]
    }
    
    print(bfs_level_order(0, graph)) 
