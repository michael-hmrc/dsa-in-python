# Leetcode 994 - Rotting Oranges
# BFS (multi-source BFS) problem.
# We start from ALL rotten oranges and spread rot level-by-level (minute-by-minute).

from collections import deque

def rotting_oranges(grid):
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0

    # Step 1: Count fresh oranges and add all initial rotten ones to the queue.
    # This makes it a *multi-source BFS*, because we start BFS from many cells at once.
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))  # (row, col, minute)
            elif grid[r][c] == 1:
                fresh += 1

    minutes = 0

    # Step 2: BFS to rot neighboring oranges
    # Each rotten orange spreads rot to adjacent fresh ones in 4 directions.
    while queue:
        r, c, time = queue.popleft()
        minutes = max(minutes, time)  # Track the maximum minute reached

        # Explore neighbors (up, down, left, right)
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc

            # If neighbor is in bounds and is a fresh orange:
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2      # Fresh -> Rotten
                fresh -= 1            # One less fresh orange remaining
                queue.append((nr, nc, time + 1))  # Rot spreads after +1 minute

    # Step 3: If no fresh oranges remain, return minutes. Otherwise, some were unreachable.
    return minutes if fresh == 0 else -1
