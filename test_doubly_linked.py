import pytest
from doubly_linked import DL_List
from doubly_linked import DL_Node


@pytest.fixture
def pop_list(request):
    l = DL_List()
    l.insert(5)
    l.insert(True)
    l.insert("Hello")
    l.insert("Yay")
    l.insert(False)
    return l


def test_doubly_linked_list(request):
    test_node = DL_Node(5)
    assert test_node.val == 5
    assert test_node.next is None
    assert test_node.prev is None


def test_doubly_linked_node(request):
    test_list = DL_List()
    assert test_list.head is None
    assert test_list.tail is None


def test_insert(request, pop_list):
    pop_list.insert("New Val")
    assert pop_list.head.val == "New Val"


def test_append(request, pop_list):
    pop_list.append("New Val")
    assert pop_list.tail.val == "New Val"


def test_pop(request, pop_list):
    assert pop_list.pop() == 5
    assert pop_list.head.val is True


def test_shift(request, pop_list):
    assert pop_list.shift() is False
    assert pop_list.tail.val == "Yay"


def test_remove(request, pop_list):
    pop_list.remove("Hello")
    with pytest.raises(AttributeError):
        pop_list.remove("Hello")
