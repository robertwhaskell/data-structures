from quick_sort import quick_sort


def test_quick_sort_on_empty():
    assert quick_sort([]) == []


def test_quick_sort_on_list_length_one():
    assert quick_sort([1]) == [1]


def test_quick_sort_on_unordered_list():
    assert quick_sort([4, 1, 9, 200, 15]) == [1, 4, 9, 15, 200]


def test_quick_sort_on_ordered_list():
    assert quick_sort([1, 2, 2, 3, 4]) == [1, 2, 2, 3, 4]


def test_quick_sort_on_reverse_order_list():
    assert quick_sort([4, 3, 2, 1, 1]) == [1, 1, 2, 3, 4]


def test_quick_sort_strings():
    assert quick_sort(['a', 'd', 'b', 'c']) == ['a', 'b', 'c', 'd']
