import pytest
from priority_queue import Priority_Queue, PNode


@pytest.fixture()
def populated_queue():
    pq = Priority_Queue()
    pq.insert(PNode(100, 10))
    pq.insert(PNode(150, 1))
    pq.insert(PNode("Hello", 30))
    pq.insert(PNode(False, 2000))
    return pq


def test_pop(populated_queue):
    assert populated_queue.pop().val is False
    assert populated_queue.pop().val == "Hello"
    assert populated_queue.pop().val == 100
    assert populated_queue.pop().val == 150


def test_peek(populated_queue):
    assert populated_queue.peek() is False


def test_insert(populated_queue):
    populated_queue.insert(PNode(True, 10000000))
    assert populated_queue.peek() is True


def test_order(populated_queue):
    l = []
    for thing in populated_queue.priority_list:
        l.append(thing.val)
    print l
    assert l == [0, False, "Hello", 100, 150]


def test_insert_into_empty_queue():
    pq = Priority_Queue()
    pq.insert(PNode('thirty', 30))
    assert pq.peek() == 'thirty'


def pop_off_empty_queue():
    pq = Priority_Queue()
    with pytest.raises(IndexError):
        pq.pop()
