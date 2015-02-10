class DL_Node(object):
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class DL_List(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert(self, val):
        if self.head:
            self.head.next = DL_Node(val, None, self.head)
            self.head = self.head.next
        else:
            self.head = self.tail = DL_Node(val)

    def append(self, val):
        if self.tail:
            self.tail.prev = DL_Node(val, self.tail, None)
            self.tail = self.tail.prev
        else:
            self.tail = self.head = DL_Node(val)

    def remove(self, val):
        iter_node = self.head
        while iter_node:
            if iter_node.val == val:
                if iter_node.next:
                    iter_node.next.prev = iter_node.prev
                if iter_node.prev:
                    iter_node.prev.next = iter_node.next
                return
            iter_node = iter_node.next
        raise AttributeError("Value not found")

    def pop():
        pass

    def shift():
        pass




