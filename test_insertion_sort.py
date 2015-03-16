from insertion_sort import insertion_sort


def test_insertion_sort_on_empty_list():
    assert insertion_sort([]) == []


def test_insertion_sort_on_list_length_one():
    assert insertion_sort([1]) == [1]


def test_insertion_sort_on_unordered_list():
    assert insertion_sort([4, 1, 9, 200, 15]) == [1, 4, 9, 15, 200]


def test_insertion_sort_on_ordered_list():
    assert insertion_sort([1, 2, 2, 3, 4]) == [1, 2, 2, 3, 4]


def test_insertion_sort_on_reverse_order_list():
    assert insertion_sort([4, 3, 2, 1, 1]) == [1, 1, 2, 3, 4]


def test_insertion_sort_strings():
    assert insertion_sort(['a', 'd', 'b', 'c']) == ['a', 'b', 'c', 'd']

