class Tnode(object):
    """Binary Tree Node Object"""
    def __init__(self, val=None, parent=None, is_right=False, is_left=False):
        self.val = val
        self.right_child = None
        self.left_child = None
        self.is_right = is_right
        self.is_left = is_left
        self.parent = parent


class BinaryTree(object):
    """Implementaion of a binary tree with methods to manipulate said tree"""
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, val):
        """Insert the value into the tree"""
        if not self.root:
            self.root = Tnode(val)
            self.size += 1
        else:
            node = self.root
            while node:
                if val > node.val:
                    if node.right_child:
                        node = node.right_child
                    else:
                        node.right_child = Tnode(val=val,
                                                 parent=node,
                                                 is_right=True)
                        self.size += 1
                        break
                elif val < node.val:
                    if node.left_child:
                        node = node.left_child
                    else:
                        node.left_child = Tnode(val=val,
                                                parent=node,
                                                is_left=True)
                        self.size += 1
                        break
                elif node.val == val:
                    break

    def contains(self, val):
        """If node is found in tree, return the node, else False"""
        if not self.root:
            return False
        else:
            node = self.root
            while node:
                if val > node.val:
                    if node.right_child:
                        node = node.right_child
                    else:
                        return False
                elif val < node.val:
                    if node.left_child:
                        node = node.left_child
                    else:
                        return False
                elif node.val == val:
                    return node

    def depth(self):
        """returns number of levels in tree"""
        return self._depth_helper(self.root, 0)

    def _depth_helper(self, node, depth_count):
        """recursive helper for depth, digs through tree and counts levels"""
        if node is None:
            return depth_count
        else:
            return max(self._depth_helper(node.left_child, depth_count + 1),
                       self._depth_helper(node.right_child, depth_count + 1))

    def balance(self):
        """Return positive if left side is higher,
        negative if right side is."""
        try:
            left_side = self._depth_helper(self.root.left_child, 1)
            right_side = self._depth_helper(self.root.right_child, 1)
        except AttributeError:
            return 0
        return left_side - right_side

    def in_order(self):
        """Returns a list of all nodes in the order of left-child, parent,
        right-child, recursively"""
        for n in self._in_order_helper(self.root):
            yield n.val

    def _in_order_helper(self, node):
        """Helper for in_order"""
        if node is None:
            return
        for n in self._in_order_helper(node.left_child):
            yield n
        yield node
        for n in self._in_order_helper(node.right_child):
            yield n

    def pre_order(self):
        """Return a list of all nodes in the order of parent, then left-child,
        then right-child, recursively"""
        for n in self._pre_order_helper(self.root):
            yield n.val

    def _pre_order_helper(self, node):
        """Helper for pre_order"""
        if node is None:
            return
        yield node
        for n in self._pre_order_helper(node.left_child):
            yield n
        for n in self._pre_order_helper(node.right_child):
            yield n

    def post_order(self):
        """Return a list of all nodes in the order of left-child, then
        right-child, then parent, recursively"""
        for n in self._post_order_helper(self.root):
            yield n.val

    def _post_order_helper(self, node):
        """post_order helper"""
        if node is None:
            return
        for n in self._post_order_helper(node.left_child):
            yield n
        for n in self._post_order_helper(node.right_child):
            yield n
        yield node

    def breadth_first(self):
        """Return a list of nodes in level-order, from left to right"""
        if self.root is None:
            return
        for n in self._breadth_first_helper(self.root):
            yield n.val

    def _breadth_first_helper(self, node):
        """breadth_first helper"""
        from collections import deque
        q = deque([node])
        while len(q) > 0:
            root = q.popleft()
            yield root
            if root.left_child:
                q.append(root.left_child)
            if root.right_child:
                q.append(root.right_child)

    def delete(self, val):
        """Remove a node from the tree if it exists, connect child nodes to new
        parents"""
        node = self.contains(val)
        try:
            if node:
                self.size -= 1
            # found node.
            # if node has no kids, remove node:
            if node.right_child is None and node.left_child is None:
                if node.is_left:
                    node.parent.left_child = None
                elif node.is_right:
                    node.parent.right_child = None
                return
            else:
                swap_node = self._find_second_largest(node)
                node.val = swap_node.val
                if swap_node.is_left:
                    if swap_node.left_child:
                        swap_node.parent.left_child = swap_node.left_child
                    else:
                        swap_node.parent.left_child = swap_node.right_child
                elif swap_node.is_right:
                    if swap_node.left_child:
                        swap_node.parent.right_child = swap_node.left_child
                    else:
                        swap_node.parent.right_child = swap_node.right_child
                return
        except AttributeError:
            return

    def _find_second_largest(self, node):
        """Helper method for delete"""
        # value has been found, find the next largest node
        largest_child = node.right_child
        iter_node = node.left_child
        while iter_node:
            largest_child = iter_node
            iter_node = iter_node.right_child
        return largest_child

    def balance_tree(self):
        """returns a balanced tree, with a depth no greater than abs[1]"""
        genlist = []
        for n in self.in_order():
            genlist.append(n)
        self._make_balanced_tree(genlist)
        return self

    def _make_balanced_tree(self, value_list):
        """takes an ordered list of values, then reconstructs our tree 
        so that it's balanced"""
        try:
            self.root = Tnode(val=value_list[len(value_list)/2])
            left_list = value_list[:(len(value_list)/2)]
            right_list = value_list[(len(value_list)/2 + 1):]
            while len(left_list) > 0:
                self.insert(left_list.pop(len(left_list)/2))
                if len(right_list) > 0:
                    self.insert(right_list.pop(len(right_list)/2))
        except IndexError:
            pass


if __name__ == '__main__':
    from time import time

    t = BinaryTree()
    t.insert(2)
    t.insert(3)
    t.insert(4)
    t.insert(5)
    t.insert(6)
    t.insert(7)
    t.insert(8)

    timer = time()
    t.contains(8)
    print "worst performance: "+str(time() - timer)

    t = BinaryTree()
    t.insert(5)
    t.insert(7)
    t.insert(3)
    t.insert(2)
    t.insert(4)
    t.insert(6)
    t.insert(8)

    timer = time()
    t.contains(8)
    print "best performance: "+str(time() - timer)
