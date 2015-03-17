def insertion_sort(unordered_list):

    for i in range(len(unordered_list)):
        moving = i
        while moving > 0 and (unordered_list[moving] < unordered_list[moving - 1]):
            (unordered_list[moving],
             unordered_list[moving - 1]) = (unordered_list[moving - 1],
                                            unordered_list[moving])
            moving -= 1
    return unordered_list


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
