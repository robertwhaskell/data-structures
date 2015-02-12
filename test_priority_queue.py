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
    l = []
    for thing in populated_queue.priority_list:
        l.append(thing.val)
    print l
    assert populated_queue.pop().val == l[1]
    l = []
    for thing in populated_queue.priority_list:
        l.append(thing.val)
    print l
    assert populated_queue.pop().val == l[1]


def test_peek(populated_queue):
    assert populated_queue.peek() == False


def test_insert(populated_queue):
    populated_queue.insert(PNode(True, 10000000))
    assert populated_queue.peek() == True


def test_order(populated_queue):
    l = []
    for thing in populated_queue.priority_list:
        l.append(thing.val)
    print l
    assert l == [0, False, "Hello", 100, 150]
