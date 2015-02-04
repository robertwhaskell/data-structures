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
        new_node = Node(val, self.head)
        #make its next value equal to the head
        #make this new node the head
        self.head = new_node

    def pop(self):
        #make a node that has the value of the head
        head_val = self.head.val
        #make the head's head the head
        self.head = self.head.next
        return head_val

    def size(self):
        #iterate through each and count.
        iter_node = self.head
        count = 0
        while iter_node is not None:
            count += 1
            iter_node = iter_node.next
        return count

    def search(self, val):
        #iterate through the list
        iter_node = self.head
        while iter_node is not None:
            if iter_node.val == val:
                return iter_node
            iter_node = iter_node.next
        return None
        #check each value
        #if we find the value, return the node
        #if we don't find it, return None.

    def remove(self, node):
        #search for the node to be removed
        iter_node = self.head
        if iter_node is node:
            self.head = self.head.next
            return
        while iter_node is not None:
            if iter_node.next is node:
                iter_node.next = iter_node.next.next
                return
            iter_node = iter_node.next
        #if we don't find it, return None
        #if we do find it, remove it

    def display(self):
        #iterate though the list
        tup = ()
        iter_node = self.head
        while iter_node is not None:
            tup = tup + (iter_node.val,)
            iter_node = iter_node.next
        return tup






