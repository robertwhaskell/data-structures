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


def test_contains(simple_tree):
    assert simple_tree.contains(5)
    assert simple_tree.contains(17)
    assert simple_tree.contains(10)


def test_size_on_empty_tree(empty_tree):
    assert empty_tree.size() == 0


def test_size_on_simple_tree(simple_tree):
    assert simple_tree.size() == 4


def test_depth_on_empty_tree(empty_tree):
    assert empty_tree.depth() == 0


def test_depth_on_simple_tree(simple_tree):
    assert simple_tree.depth() == 3


def test_balance():
    pass
