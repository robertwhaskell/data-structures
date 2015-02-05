import pytest
from stack import Node, Stack

@pytest.fixture()
def fix_empty_stack(request):
    empty_stack = Stack()
    return empty_stack


@pytest.fixture()
def fix_populated_stack(request):
    populated_stack = Stack()
    populated_stack.push(5)
    populated_stack.push("Hello")
    populated_stack.push(True)


def test_Node():
    test1 = Node()
    assert test1.val is None
    assert test1.next is None
    test2 = Node(5)
    assert test2.val == 5
    assert test2.next is None
    test3 = Node(5, test1)
    assert test3.val == 5
    assert test3.next == test1


def test_list():
    testnode = Node(5)
    test1 = Stack()
    assert test1.head is None
    test2 = Stack(testnode)
    assert test2.head == testnode

