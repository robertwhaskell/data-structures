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
    pivot_index = ((lo + hi)/2)
    pivot_value = array[pivot_index]
    array[pivot_index], array[hi] = array[hi], array[pivot_index]
    stored_index = lo
    for i in range(lo, hi + 1):
        if array[i] < pivot_value:
            array[i], array[stored_index] = array[stored_index], array[i]
            stored_index += 1
    array[stored_index], array[hi] = array[hi], array[stored_index]
    return stored_index


if __name__ == "__main__":
    from time import time

    l = range(100000)

    timer = time()
    quick_sort(l)
    print "best case: "+str(time() - timer)

    def shitty_quick_sort(array):
        return _quick_sort_helper(array, 0, (len(array) - 1))

    def shitty_quick_sort_helper(array, lo, hi):
        if lo < hi:
            partition = _partition(array, lo, hi)
            _quick_sort_helper(array, lo, (partition - 1))
            _quick_sort_helper(array, (partition + 1), hi)

    def shitty_partition(array, lo, hi):
        """same as non-shitty partition, but selects lowest index"""
        pivot_index = hi
        pivot_value = array[pivot_index]
        array[pivot_index], array[hi] = array[hi], array[pivot_index]
        stored_index = lo
        for i in range(lo, hi + 1):
            if array[i] < pivot_value:
                array[i], array[stored_index] = array[stored_index], array[i]
                stored_index += 1
        array[stored_index], array[hi] = array[hi], array[stored_index]
        return stored_index

    timer = time()
    shitty_quick_sort(l)
    print "worst case: "+str(time() - timer)
