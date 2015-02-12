import pytest
from priority_queue import Priority_Queue, PNode

@pytest.fixture()
def populated_queue():
    pq = Priority_Queue()
    pq.insert(PNode(100, 10))
    pq.insert(PNode(150, 1))
    pq.insert(PNode("Hello", 30))
    return pq


def test_pop(populated_queue):
    assert populated_queue.pop() == "Hello"


def test_peek(populated_queue):
    assert populated_queue.peek() == "Hello"


def test_insert(populated_queue):
    populated_queue.insert(PNode(True, 10000000))
    assert populated_queue.peek() == True


def test_order(populated_queue):
    print populated_queue.priority_list
    assert populated_queue.pop() == "Hello"
    assert populated_queue.pop() == 100
    assert populated_queue.pop() == 150