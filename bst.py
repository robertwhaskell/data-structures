class Tnode(object):
    """Binary Tree Node Object"""
    def __init__(self, val):
        self.val = val
        self.right_child = None
        self.left_child = None


class BinaryTree(object):
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
                        node.right_child = Tnode(val)
                        self.size += 1
                        break
                elif val < node.val:
                    if node.left_child:
                        node = node.left_child
                    else:
                        node.left_child = Tnode(val)
                        self.size += 1
                        break
                elif node.val == val:
                    break

    def contains(self, val):
        """If node is found in tree, return true, else false"""
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
                    return True

    def depth(self):
        """returns number of levels in tree"""
        return self._depth_helper(self.root, 0)

    def _depth_helper(self, node, depth_count):
        """recursive heler for depth, digs through tree and counts levels"""
        if node is None:
            return depth_count
        else:
            return max(self._depth_helper(node.left_child, depth_count + 1),
                       self._depth_helper(node.right_child, depth_count + 1))

    def balance(self):
        """Return positive if left side is higher, 
        negitive if right side is."""
        try:
            left_side = self._depth_helper(self.root.left_child, 1)
            right_side = self._depth_helper(self.root.right_child, 1)
        except AttributeError:
            return 0
        return left_side - right_side

    def in_order(self):
        for n in self._in_order_helper(self.root, []):
            yield n.val

    def _in_order_helper(self, node, orderlist):
        if node is None:
            return orderlist
        orderlist = self._in_order_helper(node.left_child, orderlist)
        if node not in orderlist:
            orderlist.append(node)
        orderlist = self._in_order_helper(node.right_child, orderlist)
        return orderlist

    def pre_order(self):
        for n in self._pre_order_helper(self.root, []):
            yield n.val

    def _pre_order_helper(self, node, orderlist):
        if node is None:
            return orderlist
        if node not in orderlist:
            orderlist.append(node)
        orderlist = self._pre_order_helper(node.left_child, orderlist)
        orderlist = self._pre_order_helper(node.right_child, orderlist)
        return orderlist

    def post_order(self):
        for n in self._post_order_helper(self.root, []):
            yield n.val

    def _post_order_helper(self, node, orderlist):
        if node is None:
            return orderlist
        orderlist = self._post_order_helper(node.left_child, orderlist)
        orderlist = self._post_order_helper(node.right_child, orderlist)
        if node not in orderlist:
            orderlist.append(node)
        return orderlist

    def breadth_first(self):
        if self.root is None:
            return
        for n in self._breadth_first_helper(self.root):
            yield n.val

    def _breadth_first_helper(self, node):
        from collections import deque
        visited = []
        q = deque([node])
        while len(q) > 0:
            root = q.popleft()
            if root not in visited:
                visited.append(root)
            if root.left_child:
                q.append(root.left_child)
            if root.right_child:
                q.append(root.right_child)
        return visited

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
