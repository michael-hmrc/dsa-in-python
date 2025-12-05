class TreeNode:

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


@staticmethod
def inorder(root: TreeNode):
    result = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.value)
        dfs(node.right)

    dfs(root)
    return result


@staticmethod
def preorder(root: TreeNode):
    result = []

    def dfs(node):
        if not node:
            return
        result.append(node.value)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return result


@staticmethod
def preorder(root: TreeNode):
    result = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        result.append(node.value)

    dfs(root)
    return result


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(preorder(root))  # [1, 2, 4, 5, 3]
    print(inorder(root))  # [4, 2, 5, 1, 3]
    print(postorder(root))  # [4, 5, 2, 3, 1]
