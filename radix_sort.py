def radix_sort(array):

    buckets = [[]] * 10
    tens_place = -1

    while True:
        tens_place += 1
        for val in array:
            try:
                buckets[int(str(val)[tens_place])].append(array.remove(val))
            except IndexError:
                pass

        pass


if __name__ == "__main__":
    pass
