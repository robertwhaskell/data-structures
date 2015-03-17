from merge_sort import merge_sort


def test_merge_sort_on_empty_list():
    assert merge_sort([]) == []


def test_merge_sort_on_list_length_one():
    assert merge_sort([1]) == [1]


def test_merge_sort_on_unordered_list():
    assert merge_sort([4, 1, 9, 200, 15]) == [1, 4, 9, 15, 200]


def test_merge_sort_on_ordered_list():
    assert merge_sort([1, 2, 2, 3, 4]) == [1, 2, 2, 3, 4]


def test_merge_sort_on_reverse_order_list():
    assert merge_sort([4, 3, 2, 1, 1]) == [1, 1, 2, 3, 4]


def test_merge_sort_strings():
    assert merge_sort(['a', 'd', 'b', 'c']) == ['a', 'b', 'c', 'd']
