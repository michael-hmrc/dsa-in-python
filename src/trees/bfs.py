from collections import deque
from typing import Any


class Node:
    def __init__(self, value):
        self.value = value
        self.neighbours = []

    def add_neighbour(self, neighbour_node):
        self.neighbours.append(neighbour_node)


def bfs(start_node):
    visited: set[Any] = set()
    queue: deque[Any] = deque([start_node])
    visited.add(start_node)

    while queue:
        node = queue.popleft()
        print(node.value, end=" ")

        for neighbour in node.neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)


if __name__ == "__main__":

    # Creating nodes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)

    # Adding neighbors
    node1.add_neighbour(node2)
    node1.add_neighbour(node3)
    node2.add_neighbour(node4)
    node2.add_neighbour(node5)
    node3.add_neighbour(node6)

    # Creating nodes
    nodeA = Node("A")
    nodeB = Node("B")
    nodeC = Node("C")
    nodeD = Node("D")
    nodeE = Node("E")
    nodeF = Node("F")
    nodeG = Node("G")

    # Adding neighbors

    #       A
    #      / \
    #     B   C
    #    / \   \
    #   D   E   F
    #        \
    #         G

    nodeA.add_neighbour(nodeB)
    nodeA.add_neighbour(nodeC)
    nodeB.add_neighbour(nodeD)
    nodeB.add_neighbour(nodeE)
    nodeC.add_neighbour(nodeF)
    nodeE.add_neighbour(nodeG)

    print("BFS Traversal: ")
    bfs(nodeA)  # Output: A B C D E F

# print("\nDFS Traversal: ")
# dfs(nodeA)  # Output: A B D E F C
