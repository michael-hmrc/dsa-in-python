
# You must know how to build an adjacency list, because almost all problems use it.

# Adjacency List (most important)
# A graph is a dictionary where each node points to a list of its neighbors:

# We will focus on Adjacency List, because it's:

# - easy to build
# - uses little memory
# - works for ALL graph algorithms


graph = {
    0: [1, 2],
    1: [2],
    2: [0],
    3: []
}

# Meaning:

# Node 0 connects to 1 and 2

# Node 1 connects to 2

# Node 2 connects to 0

# Node 3 has no edges

# This is the default representation for DFS, BFS, Dijkstra, etc.


# build an undirected graph

undirected_graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}


directed_graph = {
    0: [1, 3],
    1: [2],
    2: [3],
    3: []
}
