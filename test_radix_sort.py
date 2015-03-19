from radix_sort import radix_sort, radix_sort_string


def test_radix_sort_on_empty():
    assert radix_sort([]) == []


def test_radix_sort_on_list_length_one():
    assert radix_sort([1]) == [1]


def test_radix_sort_on_unordered_list():
    assert radix_sort([4, 1, 9, 200, 15]) == [1, 4, 9, 15, 200]


def test_radix_sort_on_ordered_list():
    assert radix_sort([1, 2, 2, 3, 4]) == [1, 2, 2, 3, 4]


def test_radix_sort_on_reverse_order_list():
    assert radix_sort([4, 3, 2, 1, 1]) == [1, 1, 2, 3, 4]


def test_radix_sort_strings():
    assert radix_sort_string(['a', 'd', 'b', 'c']) == ['a', 'b', 'c', 'd']


def test_radix_sort_long_string():
    assert (radix_sort_string(['Four',
                               'score',
                               'and',
                               'seven',
                               'years',
                               'ago']) ==
        ['Four', 'ago', 'and', 'score', 'seven', 'years'])

def test_radix_sort_string_empty():
    assert radix_sort_string([]) == []

