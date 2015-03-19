def radix_sort(array):
    if len(array) > 0:
        tens_place = 1
        index_num = 0
        max_val = max(array)
        while max_val > tens_place:
            buckets = [[] for x in range(10)]
            for val in array:
                index_num = val % (tens_place * 10) / tens_place
                buckets[index_num].append(val)

            transfer_list = []
            for bucket in buckets:
                for var in bucket:
                    transfer_list.append(var)

            array = transfer_list
            tens_place *= 10
    return array


def radix_sort_string(array):
    index_place = 0
    index_num = 0
    if len(array) > 0:
        longest = array[0]
        for val in array:
            if len(val) > len(longest):
                longest = val

    while index_place > len(longest):
        buckets = [[] for x in range(128)]
        for val in array:
            index_num = ord(val[index_place])
            buckets[index_num].append(val)

        transfer_list = []
        for bucket in buckets:
            for var in bucket:
                transfer_list.append(var)

        array = transfer_list
        index_place += 1
    return array


radix_sort([4, 1, 99])


if __name__ == "__main__":
    pass
