import linked_list

# test 1 - basic stuff. see if the methods work under normal duress.

n1 = linked_list.Node(5, None)
assert n1.val is 5
assert n1.next == None
n8 = linked_list.Node(53, None)

mylist = linked_list.list(n1)
assert mylist.head is not None
mylist.insert(True)
mylist.insert(500)
mylist.insert("")
mylist.insert("Thing")
mylist.insert(None)
mylist.insert(1000)

assert mylist.head.val is 1000

assert mylist.pop() is 1000

assert mylist.head.val is None

assert mylist.size() is 6

assert mylist.search(True).val is True

assert mylist.search("doesn't exist") is None

mylist.remove(n1)
mylist.remove(n8)

assert mylist.search(n1.val) is None

assert mylist.size() is 5

assert mylist.display() == "(None, 'Thing', '', 500, True)"

# test 2 - more complicated, mostly checking to see if an empty
# messes anything up.

# insertion into an empty list
mylist2 = linked_list.list(None)
mylist2.insert(67)
assert mylist2.head.val is 67

# remove only node in list

rmnode = mylist2.search(67)
mylist2.remove(rmnode)
assert mylist2.head is None

# remove node not in list

mylist2.remove(rmnode)

# pop from empty list

mylist2.pop()

# size if nothing

assert mylist2.size() is 0

# display an empty list

assert mylist2.display() == "()"

# remove something weird

mylist2.remove(True)
mylist2.remove(5)
mylist2.remove("dkdkda;fdj")

# insert a tuple

mylist2.insert((5, "blah", True))
assert mylist2.display() == "((5, 'blah', True))"
