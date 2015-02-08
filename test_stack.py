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
    return populated_stack


def test_Node():
    testnode = Node(5)
    assert testnode.val == 5
    assert testnode.next is None


def test_Node_with_next():
    testnode = Node(5)
    testnode2 = Node(6, testnode)
    assert testnode2.val == 6
    assert testnode2.next == testnode


def test_Stack():
    testnode = Node(5)
    test1 = Stack()
    assert test1.head is None
    test2 = Stack(testnode)
    assert test2.head == testnode


def test_push(fix_empty_stack, fix_populated_stack):
    fix_empty_stack.push("Thingo")
    assert fix_empty_stack.pop() == "Thingo"
    fix_populated_stack.push("Other Thingo")
    assert fix_populated_stack.pop() == "Other Thingo"


def test_pop(fix_empty_stack, fix_populated_stack):
    assert fix_populated_stack.pop() is True
    assert fix_populated_stack.pop() == "Hello"
    assert fix_populated_stack.pop() == 5
    with pytest.raises(AttributeError):
        fix_populated_stack.pop()
