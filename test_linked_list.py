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

mylist = linked_list.list(n1)

print mylist.display()

mylist.insert(True)
mylist.insert(5)
mylist.insert("")
mylist.insert("Thing")
mylist.insert(None)
mylist.insert(1000)

assert mylist.head.val is 1000

assert mylist.pop() is 1000

assert mylist.head.val is None




