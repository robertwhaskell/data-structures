from new_bin_heap import Heap
import pytest


@pytest.fixture
def empty_heap():
    h = Heap()
    return h


@pytest.fixture
def full_heap():
    h = Heap()
    h.push(100)
    h.push(19)
    h.push(36)
    h.push(17)
    h.push(3)
    h.push(25)
    h.push(1)
    h.push(2)
    h.push(7)
    return h


def test_heap():
    h = Heap()
    assert h.heapList[0] == 0
    assert h.size == 0


def test_iter_heap():
    l = [100, 19, 36, 17, 3, 25, 1, 2, 7]
    h = Heap(l)
    assert h.heapList[1] == 100
    assert h.size == 9


def test_push(empty_heap):
    empty_heap.push(25)
    assert empty_heap.heapList[1] == 25
    assert empty_heap.size == 1
    empty_heap.push(50)
    assert empty_heap.heapList[1] == 50
    assert empty_heap.heapList[2] == 25
    assert empty_heap.size == 2


def test_pop(full_heap):
    assert full_heap.pop() == 100
    assert full_heap.size == 8
    assert full_heap.pop() == 36
    assert full_heap.size == 7
    assert full_heap.pop() == 25
    assert full_heap.size == 6


def test_pop_from_empty_heap(empty_heap):
    with pytest.raises(IndexError):
        empty_heap.pop()
