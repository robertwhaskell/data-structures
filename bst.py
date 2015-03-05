class Tnode(object):
    def __init__(self, val):
        self.val = val
        self.right_child = None
        self.left_child = None


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert_helper(val, self.root)

    def _insert_helper(self, val, node):
        if node is None:
            return Tnode(val)
        else:
            if val > node.val:
                node.right_child = self._insert_helper(val, node.right_child)
            elif val < node.val:
                node.left_child = self._insert_helper(val, node.left_child)
        return node
