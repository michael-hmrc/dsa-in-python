class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    #    1
    #    / \
    #   2   3
    #  / \    \
    # 4   5    6


def preorderHelper(node: Node, result: list[int]) -> list[int]:
    if node == None:
        return
    result.append(node.value)
    preorderHelper(node.left, result)
    preorderHelper(node.right, result)


def inorderHelper(node: Node, result: list[int]) -> list[int]:
    if node == None:
        return
    inorderHelper(node.left, result)
    result.append(node.value)
    inorderHelper(node.right, result)


def postorderHelper(node: Node, result: list[int]) -> list[int]:
    if node == None:
        return
    postorderHelper(node.left, result)
    postorderHelper(node.right, result)
    result.append(node.value)


#  Root -> Left -> Right
def preorder(node: Node) -> list[int]:
    result: list[int] = []
    preorderHelper(node, result)
    return result


#  Left -> Root -> Right
def inorder(node: Node) -> list[int]:
    result: list[int] = []
    inorderHelper(node, result)
    return result


#  Left -> Right -> Root
def postorder(node: Node) -> list[int]:
    result: list[int] = []
    postorderHelper(node, result)
    return result


if __name__ == "__main__":

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    print(preorder(root))
    print(inorder(root))
    print(postorder(root))
