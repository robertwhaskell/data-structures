class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, val=None):
        self.tail = Node(val, self.tail)
        if self.head is None:
            self.head = self.tail

    def dequeue(self):
        try:
            head_val = self.head.val
            self.head = self.head.next
            return head_val
        except AttributeError:
            raise AttributeError("Empty Queue")
