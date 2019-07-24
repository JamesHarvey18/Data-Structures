class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = value
        return self.left

    def insert_right(self, value):
        self.right = value
        return self.right

    def print_tree(self):
        print(self.value)


def max_depth(node):
    if node is None:
        return 0

    l_depth = max_depth(node.left)
    r_depth = max_depth(node.right)

    return max(l_depth, r_depth) + 1


root = BinaryTreeNode(10)
a = BinaryTreeNode(1)
b = BinaryTreeNode(11)
c = BinaryTreeNode(12)
d = BinaryTreeNode(2)

root.left = a
a.right = b
b.right = c
c.left = d

print(max_depth(root))


