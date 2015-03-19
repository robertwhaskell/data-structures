def radix_sort(array):
    """a sorting algorithm that looks through an array of integers,
    and sorts them according to their base ten index"""
    if len(array) > 0:
        tens_place = 1
        index_num = 0
        max_val = max(array)
        buckets = [[] for x in range(10)]
        while max_val > tens_place:
            for val in array:
                index_num = val % (tens_place * 10) / tens_place
                buckets[index_num].append(val)

            transfer_list = []
            for bucket in buckets:
                for i in range(len(bucket)):
                    transfer_list.append(bucket.pop(0))

            array = transfer_list
            tens_place *= 10
    return array


def radix_sort_string(array):
    """a sorting algorithm for strings - works the same as radix_sort,
    except that we sort via string index, starting with the end of the
    string, ending with the beginning."""
    try:
        longest = get_longest_string(array)
    except IndexError:
        return array

    index_num = 0
    index_place = (len(longest) - 1)
    buckets = [[] for x in range(128)]

    while index_place >= 0:
        for val in array:
            try:
                index_num = ord(val[index_place])
            except IndexError:
                index_num = 0
            buckets[index_num].append(val)

        transfer_list = []
        for bucket in buckets:
            for i in range(len(bucket)):
                transfer_list.append(bucket.pop(0))
        array = transfer_list
        index_place -= 1
    return array


def get_longest_string(array):
    longest = array[0]
    for val in array:
        if len(val) > len(longest):
            longest = val
    return longest


if __name__ == "__main__":
    from time import time
    best_case = [1, 1]
    worst_case = [1, 10000000000000000000000]

    timer = time()
    radix_sort(best_case)
    print "best case: "+str(time() - timer)

    timer = time()
    radix_sort(worst_case)
    print "worst case: "+str(time() - timer)
