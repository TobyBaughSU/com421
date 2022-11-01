class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)

    def print_from(self):
        if self.left is not None:
            self.left.print_from()
        print(self.value)
        if self.right is not None:
            self.right.print_from()


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, *values):
        for value in values:
            if self.root is None:
                self.root = TreeNode(value)
            else:
                self.root.insert(value)

    def print_from(self):
        self.root.print_from()

tree = BinaryTree()
tree.insert(29, 20, 17, 40, 25, 18, 1)
tree.print_from()
