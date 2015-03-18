def quick_sort(array):
    '''Input an array, the lowest value, and the highest value. Perform a
    quicksort and return a sorted list'''
    return _quick_sort_helper(array, 0, (len(array) - 1))


def _quick_sort_helper(array, lo, hi):
    if lo < hi:
        partition = _partition(array, lo, hi)
        _quick_sort_helper(array, lo, (partition - 1))
        _quick_sort_helper(array, (partition + 1), hi)
    return array


def _partition(array, lo, hi):
    pivot_value = array[0]
    array[0], array[hi] = array[hi], array[0]
    stored_index = lo
    for i in range(len(array)):
        if array[i] < pivot_value:
            array[i], array[stored_index] = array[stored_index], array[i]
            stored_index += 1
    array[stored_index], array[hi] = array[hi], array[stored_index]
    return stored_index
