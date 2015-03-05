class Tnode(object):
    """Binary Tree Node Object"""
    def __init__(self, val):
        self.val = val
        self.right_child = None
        self.left_child = None


class BinaryTree(object):
    def __init__(self):
        self.root = None
        self.tree_size = 0

    def insert(self, val):
        """Insert the value into the tree"""
        self.root = self._insert_helper(val, self.root)
        self.tree_size += 1

    def _insert_helper(self, val, node):
        """Recursive function to place the value into the tree via the rules of
        a binary tree"""
        if node is None:
            return Tnode(val)
        else:
            if val > node.val:
                node.right_child = self._insert_helper(val, node.right_child)
            elif val < node.val:
                node.left_child = self._insert_helper(val, node.left_child)
        return node

    def contains(self, val):
        """If node is found in tree, return true, else false"""
        return self._contains_helper(val, self.root)

    def _contains_helper(self, val, node):
        if node is None:
            return False
        elif node.val == val:
            return True
        elif val < node.val:
            return self._contains_helper(val, node.left_child)
        elif val > node.val:
            return self._contains_helper(val, node.right_child)

    def size(self):
        return self.tree_size
