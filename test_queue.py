import pytest
from queue import Queue


@pytest.fixture
def populated_queue(request):
    q = Queue()
    q.enqueue(5)
    q.enqueue("True")
    q.enqueue(False)
    q.enqueue(" ")
    return q


def test_enqueue(request):
    q = Queue()
    q.enqueue(5)
    assert q.head.val == q.tail.val
    assert q.head.val == 5
    assert q.size == 1


def test_dequeue(request, populated_queue):
    assert populated_queue.dequeue() == 5
    assert populated_queue.head.val == "True"
    assert populated_queue.size == 3


def test_size(request, populated_queue):
    assert populated_queue.size == 4
    assert Queue().size == 0
