def insertion_sort(unord_list):

    for i in range(len(unord_list)):
        while i > 0 and (unord_list[i] < unord_list[i - 1]):
            unord_list[i], unord_list[i - 1] = unord_list[i - 1], unord_list[i]
            i -= 1
    return unord_list


if __name__ == "__main__":

    from time import time

    test_list = [x for x in range(10)]

    timer = time()
    insertion_sort(test_list)
    print "Best performance 10: " + str(time() - timer)

    test_list.reverse()
    timer = time()
    insertion_sort(test_list)
    print "Worst performance 10: " + str(time() - timer)

    test_list = [x for x in range(100)]

    timer = time()
    insertion_sort(test_list)
    print "Best performance 100: " + str(time() - timer)

    test_list.reverse()
    timer = time()
    insertion_sort(test_list)
    print "Worst performance 100: " + str(time() - timer)

    test_list = [x for x in range(1000)]

    timer = time()
    insertion_sort(test_list)
    print "Best performance 1000: " + str(time() - timer)

    test_list.reverse()
    timer = time()
    insertion_sort(test_list)
    print "Worst performance 1000: " + str(time() - timer)
