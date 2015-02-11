from binary_heap import Heap
from binary_heap import Node
import pytest


@pytest.fixture
def populated_heap():
    heap = Heap()
    heap.push(5)
    heap.push(10)
    heap.push(20)
    # heap.push(50)
    # heap.push(28)
    return heap


def test_Node():
    assert Node(5).val == 5


def test_Heap():
    assert Heap().head is None


def test_push_onto_empty_heap():
    heap = Heap()
    heap.push(5)
    assert heap.head.val == 5


def test_push_onto_full_heap(populated_heap):
    populated_heap.push(7)
    assert populated_heap.head.val == 20
    assert populated_heap.head.left_child == 5
    assert populated_heap.head.right_child == 10
