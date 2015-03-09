from bst import BinaryTree
import pytest


@pytest.fixture(scope="function")
def simple_tree():
    t = BinaryTree()
    t.insert(5)
    t.insert(10)
    t.insert(2)
    t.insert(17)
    return t


@pytest.fixture(scope="function")
def empty_tree():
    t = BinaryTree()
    return t


def test_binarytree():
    t = BinaryTree()
    assert t.root is None


def test_insert_into_empty_tree(empty_tree):
    empty_tree.insert(5)
    assert empty_tree.root.val == 5


def test_insert_into_simple_tree(simple_tree):
    simple_tree.insert(1)
    assert simple_tree.root.left_child.left_child.val == 1


def test_insert_duplicate(simple_tree):
    assert simple_tree.size == 4
    simple_tree.insert(17)
    assert simple_tree.size == 4


def test_contains(simple_tree):
    assert simple_tree.contains(5)
    assert simple_tree.contains(17)
    assert simple_tree.contains(10)


def test_size_on_empty_tree(empty_tree):
    assert empty_tree.size == 0


def test_size_on_simple_tree(simple_tree):
    assert simple_tree.size == 4


def test_depth_on_empty_tree(empty_tree):
    assert empty_tree.depth() == 0


def test_depth_on_simple_tree(simple_tree):
    assert simple_tree.depth() == 3


def test_balance(simple_tree):
    assert simple_tree.balance() == -1


def test_balance_empty_tree(empty_tree):
    assert empty_tree.balance() == 0


def test_balance_one_node_tree_returns_1():
    t = BinaryTree()
    t.insert(1)
    assert t.balance() == 0


def test_in_order_traversal_empty(empty_tree):
    iogen = empty_tree.in_order()
    genlist = []
    for n in iogen:
        genlist.append(n)
    assert genlist == []


def test_in_order_traversal_simple_tree(simple_tree):
    iogen = simple_tree.in_order()
    genlist = []
    for n in iogen:
        genlist.append(n)
    assert genlist == [2, 5, 10, 17]


def test_post_order_traversal_empty(empty_tree):
    iogen = empty_tree.post_order()
    genlist = []
    for n in iogen:
        genlist.append(n)
    assert genlist == []


def test_post_order_traversal_simple_tree(simple_tree):
    iogen = simple_tree.post_order()
    genlist = []
    for n in iogen:
        genlist.append(n)
    assert genlist == [2, 17, 10, 5]


def test_pre_order_traversal_empty(empty_tree):
    genlist = []
    for n in empty_tree.pre_order():
        genlist.append(n)
    assert genlist == []


def test_pre_order_traversal_simple_tree(simple_tree):
    iogen = simple_tree.pre_order()
    genlist = []
    for n in iogen:
        genlist.append(n)
    assert genlist == [5, 2, 10, 17]


def test_breadth_first_traversal_empty(empty_tree):
    iogen = empty_tree.breadth_first()
    genlist = []
    for n in iogen:
        genlist.append(n)
    assert genlist == []


def test_breadth_first_traversal_simple_tree(simple_tree):
    iogen = simple_tree.breadth_first()
    genlist = []
    for n in iogen:
        genlist.append(n)
    assert genlist == [5, 2, 10, 17]


def test_delete_empty_tree(empty_tree):
    assert empty_tree.delete(100) is None


def test_delete_on_node_with_no_children(simple_tree):
    simple_tree.delete(2)
    iogen = simple_tree.in_order()
    genlist = []
    for n in iogen:
        genlist.append(n)
    assert genlist == [5, 10, 17]


def test_delete_on_node_with_one_child(simple_tree):
    simple_tree.delete(10)
    iogen = simple_tree.in_order()
    genlist = []
    for n in iogen:
        genlist.append(n)
    assert genlist == [2, 5, 17]


def test_delete_on_node_with_two_children(simple_tree):
    simple_tree.delete(5)
    iogen = simple_tree.in_order()
    genlist = []
    for n in iogen:
        genlist.append(n)
    assert genlist == [2, 10, 17]






