class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Stack(object):
    def __init__(self, head=None):
        self.head = head

    def push(self, val=None):
        self.head = Node(val, self.head)

    def pop(self):
        try:
            head_val = self.head.val
            self.head = self.head.next
            return head_val
        except AttributeError:
            raise AttributeError("Empty Stack")
