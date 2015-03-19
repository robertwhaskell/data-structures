def radix_sort(array):

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
        if len(transfer_list) == 0:
            break

        array = transfer_list
        tens_place *= 10
    return array

radix_sort([4, 1, 99])


if __name__ == "__main__":
    pass
