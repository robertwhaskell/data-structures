class Node(object):
    def __init__(self, val, parent=None, left_child=None, right_child=None):
        self.val = val
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child


class Heap(object):
    def __init__(self):
        self.head = None

    def push(self, val):
        self.find_open_spot(self.head, val)

    def pop(self):
        pass

    def find_open_spot(self, iter_node, val):
        if not iter_node.left_child:
            iter_node.left_child = Node(val)
        else:
            self.find_open_spot(iter_node.left_child, val)
        if not iter_node.right_child:
            iter_node.right_child = Node(val)
        else:
            self.find_open_spot(iter_node.right_child, val)
