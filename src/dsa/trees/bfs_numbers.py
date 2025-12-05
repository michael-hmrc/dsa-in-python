from collections import deque


class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


def bfs(node):

    if not node:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


if __name__ == "__main__":

    # Build sample tree:
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print(bfs(root))            #     [1, 2, 3, 4, 5]
