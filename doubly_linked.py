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
        try:
            self.head.next = DL_Node(val, None, self.head)
            self.head = self.head.next
        except AttributeError:
            self.head = self.tail = DL_Node(val)

    def append(self, val):
        try:
            self.tail.prev = DL_Node(val, self.tail, None)
            self.tail = self.tail.prev
        except AttributeError:
            self.tail = self.head = DL_Node(val)

    def search(self, val):
        iter_node = self.head
        while True:
            try:
                if iter_node.val == val:
                    return iter_node
            except AttributeError:
                return AttributeError("Value not found")
            iter_node = iter_node.prev

    def remove(self, val):
        found_node = self.search(val)
        try:
            found_node.next.prev = found_node.prev
        except AttributeError:
            self.head = found_node.prev
        try:
            found_node.prev.next = found_node.next
        except AttributeError:
            self.tail = found_node.next

    def pop(self):
        try:
            head_val = self.head.val
            try:
                self.head = self.head.prev
                self.head.next = None
            except AttributeError:
                self.head = self.tail = None
            return head_val
        except AttributeError:
            raise AttributeError("This list is empty")

    def shift(self):
        try:
            tail_val = self.tail.val
            try:
                self.tail = self.tail.next
                self.tail.prev = None
            except AttributeError:
                self.tail = self.head = None
            return tail_val
        except AttributeError:
            raise AttributeError("This list is empty")
