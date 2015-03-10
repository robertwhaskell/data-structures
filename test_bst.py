from bst import BinaryTree
import pytest


@pytest.fixture(scope="function")
def unbalanced_tree():
    t = BinaryTree()
    t.insert(5)
    t.insert(6)
    t.insert(7)
    t.insert(8)
    t.insert(9)
    t.insert(4)
    return t


@pytest.fixture(scope="function")
def balanced_tree():
    t = BinaryTree()
    t.insert(5)
    t.insert(2)
    t.insert(1)
    t.insert(3)
    t.insert(8)
    t.insert(7)
    t.insert(9)
    return t


@pytest.fixture(scope="function")
def complex_tree():
    t = BinaryTree()
    t.insert(100)
    t.insert(80)
    t.insert(60)
    t.insert(40)
    t.insert(20)
    t.insert(50)
    t.insert(70)
    t.insert(90)
    t.insert(85)
    t.insert(95)
    t.insert(120)
    t.insert(140)
    t.insert(160)
    t.insert(180)
    t.insert(110)
    t.insert(175)
    t.insert(170)
    t.insert(176)
    return t


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


def test_contains_works_with_0_node(simple_tree):
    simple_tree.insert(0)
    assert simple_tree.contains(0)


def test_contains_with_non_existent_node(simple_tree):
    assert simple_tree.contains(42) is False


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


def test_delete_on_complex_tree_root(complex_tree):
    complex_tree.delete(100)
    iogen = complex_tree.in_order()
    genlist = []
    for n in iogen:
        genlist.append(n)
    assert genlist == [20, 40, 50, 60, 70, 80, 85, 90, 95, 110, 120, 140, 160,
                       170, 175, 176, 180]


def test_delete_sequence_complex_tree(complex_tree):
    complex_tree.delete(100)
    complex_tree.delete(120)
    complex_tree.delete(80)
    complex_tree.delete(180)
    iogen = complex_tree.in_order()
    genlist = []
    for n in iogen:
        genlist.append(n)
    assert genlist == [20, 40, 50, 60, 70, 85, 90, 95, 110, 140, 160,
                       170, 175, 176]


def test_delete_keeps_size_accurate(complex_tree):
    assert complex_tree.size == 18
    iogen = complex_tree.in_order()
    genlist = []
    for n in iogen:
        genlist.append(n)
    complex_tree.delete(100)
    complex_tree.delete(120)
    complex_tree.delete(80)
    assert 15 == complex_tree.size


def test_unbalanced_tree_balancing(unbalanced_tree):
    assert unbalanced_tree.balance() == -3
    unbalanced_tree.balance_tree()
    b = unbalanced_tree.balance()
    assert b < 2 and b > -2


def test_balanced_tree_balancing(balanced_tree):
    assert balanced_tree.balance() == 0
    b = balanced_tree.balance_tree()
    balanced_tree == b


def test_balance_tree_empty_tree(empty_tree):
    assert empty_tree.balance() == 0
    empty_tree.balance()
    assert empty_tree.balance() == 0
