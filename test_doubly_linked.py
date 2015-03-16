import pytest
from doubly_linked import DL_List
from doubly_linked import DL_Node


@pytest.fixture()
def pop_list(request):
    l = DL_List()
    l.insert(5)
    l.insert(True)
    l.insert("Hello")
    l.insert("Yay")
    l.insert(False)
    return l


def test_doubly_linked_list():
    test_node = DL_Node(5)
    assert test_node.val == 5
    assert test_node.next is None
    assert test_node.prev is None


def test_doubly_linked_node():
    test_list = DL_List()
    assert test_list.head is None
    assert test_list.tail is None


def test_insert(pop_list):
    pop_list.insert("New Val")
    assert pop_list.head.val == "New Val"


def test_append(pop_list):
    pop_list.append("New Val")
    assert pop_list.tail.val == "New Val"


def test_pop(pop_list):
    assert pop_list.pop() is False
    assert pop_list.head.val is "Yay"


def test_shift(pop_list):
    assert pop_list.shift() == 5
    assert pop_list.tail.val is True


def test_remove(pop_list):
    pop_list.remove("Hello")
