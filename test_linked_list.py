import linked_list

n1 = linked_list.Node(5, None)
n2 = linked_list.Node(23948.398, None)
n3 = linked_list.Node(True, None)
n4 = linked_list.Node(False, None)
n5 = linked_list.Node("Hey there!", None)
n6 = linked_list.Node("sdkfsdlfh2[03u", None)
n7 = linked_list.Node("", None)
n8 = linked_list.Node(None, None)
n9 = linked_list.Node(0, None)

#test 1

mylist = linked_list.list(n1)
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

assert mylist.display() == (None, 'Thing', '', 500, True,)

