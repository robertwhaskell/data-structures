class Node(object):
    def __init__(self, val, next):
        super(Node, self).__init__()
        self.val = val
        self.next = next


class list(object):
        def __init__(self, head):
            super(list, self).__init__()
            self.head = head

        def insert(self, val):
            #make a new node with the Value
            newNode = Node(val, self.head)
            #make its next value equal to the head
            #make this new node the head
            self.head = newNode
        
