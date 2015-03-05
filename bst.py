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
        if not self.contains(val):
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
        """recursive helper for contains that digs through tree for value"""
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

    def depth(self):
        """returns number of levels in tree"""
        return self._depth_helper(self.root, 0)

    def _depth_helper(self, node, depth_count):
        """recursive heler for depth, digs through tree and counts levels"""
        if node is None:
            return depth_count
        else:
            left_depth = self._depth_helper(node.left_child, depth_count + 1)
            right_depth = self._depth_helper(node.right_child, depth_count + 1)
            if left_depth > right_depth:
                return left_depth
            else:
                return right_depth

    def balance(self):
        """Return positive if left side is higher, negitive if right side is."""
        try:
            left_side = self._depth_helper(self.root.left_child, 1)
            print("testsfksdjfdskjfkd")
            print self.root.right_child
            right_side = self._depth_helper(self.root.right_child, 1)
        except AttributeError:
            print('empty')
            return 0
        return left_side - right_side

if __name__ == '__main__':
    from time import time
    import random
    nums = random.sample(range(1, 1000000), 999999)
    t = BinaryTree()

    timer = time()
    t.insert(50.1)
    t.contains(50.1)
    print 'searches for thing that exists:'+str(time() - timer)
    timer = time()
    t.contains(.1)
    print 'searches for thing that does not exit:'+str(time() - timer)
