
# Leetcode 200 - Number of Islands

from collections import deque

# 1 = land
# 0 = water

#   1 1 0 0 0
#   1 1 0 1 1
#   0 0 0 1 1

# An island = a group of connected lands (up, down, left, right).

# Your job:

# Count how many separate islands exist.
# In the above:
# Island 1: top-left 4 cells
# Island 2: the 4 cells on the right

# Answer = 2

# KEY INSIGHT (MOST IMPORTANT)

# A grid is a graph.
# Each cell is a node.
# Neighbors are up/down/left/right.

# We use BFS or DFS to explore an entire island.


def num_islands(grid):
    
    # base check
    if not grid:
        return 0

    # get sizes and setup 
    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    # explore one full island 
    def bfs(r, c):
        queue = deque([(r, c)])
        visited.add((r, c))

        # traverse the island
        while queue:
            x, y = queue.popleft()
            # check it's four neighbours
            for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                nx, ny = x + dx, y + dy
                if (0 <= nx < rows and 0 <= ny < cols and
                    grid[nx][ny] == "1" and
                    (nx, ny) not in visited):
                    visited.add((nx, ny))
                    queue.append((nx, ny))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                bfs(r, c)
                islands += 1

    return islands
