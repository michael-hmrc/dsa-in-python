# DFS is the foundation of almost everything.

# We learn:

# How to avoid infinite loops (using visited)

# How to traverse neighbors

# How recursion handles depth-first search

#  this is the pattern of dfs

# Template:

# def dfs(node):
#     if node in visited:
#         return
#     visited.add(node)

#     for nei in graph[node]:
#         dfs(nei)


graph = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}


# What DFS Does

# DFS explores a graph by going:

# As deep as possible before backtracking.

# It works like exploring a maze:
# keep going forward until you hit a dead end, then backtracking

# DFS Key Idea

# Use a visited set to avoid infinite loops
# Recursively explore neighbors
# Stop revisiting old nodes

# Our graph

# 0 -- 1
# |    |
# 3 -- 2

visited = set()


def dfs(node):

    if node in visited:
        return

    visited.add(node)
    print(node)  # process the node (optional)

    for nei in graph[node]:
        dfs(nei)


if __name__ == "__main__":
    print(dfs(0))
