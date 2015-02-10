class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.list_size = 0

    def enqueue(self, val=None):
        if self.tail:
            self.tail.next = Node(val)
            self.tail = self.tail.next
        else:
            self.tail = self.head = Node(val)
        self.list_size += 1

    def dequeue(self):
        try:
            head_val = self.head.val
            self.head = self.head.next
            self.list_size -= 1
            return head_val
        except AttributeError:
            raise AttributeError("Empty Queue")

    def size(self):
        return self.list_size
