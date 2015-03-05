from bst import BinaryTree
import pytest

@pytest.fixture()
def simple_tree():
    t = BinaryTree()
    t.insert(5)
    t.insert(10)
    t.insert(2)
    t.insert(17)
    return t


def test_binarytree():
    t = BinaryTree()
    assert t.root == None


def test_insert_into_empty_tree():
    t = BinaryTree()
    t.insert(5)
    assert t.root.val == 5


def test_insert_into_simple_tree(simple_tree):
    simple_tree.insert(1)
    assert simple_tree.root.left_child.left_child.val == 1


def test_contains():
    pass


def test_size():
    pass


def test_depth():
    pass


def test_balance():
    pass
