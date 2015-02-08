class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class list(object):
    def __init__(self, head=None):
        self.head = head
        self.list_size = 0
        if self.head:
            self.list_size = 1

    def insert(self, val):
        # make a new node with the Value
        # make its next value equal to the head
        # make this new node the head
        self.head = Node(val, self.head)
        self.list_size += 1

    def pop(self):
        # make a node that has the value of the head
        # make the head's head the head
        # if self.head is not None:
        try:
            head_val = self.head.val
            self.head = self.head.next
            self.list_size -= 1
            return head_val
        except AttributeError:
            raise ValueError(u"No head in this list.")

    def size(self):
        # iterate through each and add to count.
        # iter_node = self.head
        # count = 0
        # while iter_node is not None:
        #     count += 1
        #     iter_node = iter_node.next
        # return count
        return self.list_size

    def search(self, val):
        # iterate through the list
        # check each value
        # if we find the value, return the node
        # if we don't find it, return None.
        iter_node = self.head
        while iter_node is not None:
            if iter_node.val == val:
                return iter_node
            iter_node = iter_node.next
        return None

    def remove(self, node):
        # search for the node to be removed
        # if we don't find it, return None
        # if we do find it, remove it
        iter_node = self.head
        if iter_node is node:
            self.head = self.head.next
            self.list_size -= 1
            return
        while iter_node is not None:
            if iter_node.next is node:
                iter_node.next = iter_node.next.next
                self.list_size -= 1
                return
            iter_node = iter_node.next

    def display(self):
        # iterate though the list
        # add the values of each node
        # to the tuple, then display.
        output_string = u""
        iter_node = self.head
        while iter_node:
            if isinstance(iter_node.val, str):
                convert = iter_node.val.decode('utf-8')
                output_string = u"{}'{}'".format(output_string, convert)
            elif isinstance(iter_node.val, unicode):
                output_string = u"{}'{}'".format(output_string, iter_node.val)
            else:
                output_string = u"{}{}".format(output_string, iter_node.val)
            iter_node = iter_node.next
            if iter_node:
                output_string = u"{}, ".format(output_string)
            else:
                return u"({})".format(output_string)
        return u"()"

    def __str__(self):
        return str(self.display(), 'utf-8')

    def __repr__(self):
        return str(self.display(), 'utf-8')
