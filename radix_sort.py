def radix_sort(array):
    buckets = [[]] * 10
    tens_place = 1
    index_num = 0
    while True:
        for val in array:
            index_num = val % (tens_place * 10) / tens_place
            buckets[index_num].append(val)

        transfer_list = []
        for bucket in buckets:
            for var in bucket:
                transfer_list.append(var)
        if len(transfer_list) == 0:
            break

        array += transfer_list

if __name__ == "__main__":
    pass
