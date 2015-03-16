def insertion_sort(unordered_list):
    # inspect the first value in the list.
    # if that value if larger than the next value in the list,
    # swap them. If not, leave it be.
    for i in range(len(unordered_list)):
        try:
            moving = i + 1
            while (unordered_list[moving] < unordered_list[moving - 1]):
                (unordered_list[moving],
                 unordered_list[moving - 1]) = (unordered_list[moving - 1],
                                                unordered_list[moving])
                if moving > 1:
                    moving -= 1
                else:
                    break
        except IndexError:
            return unordered_list
    return []


if __name__ == "__main__":
# show the time it takes to run a best case and worst case scenerio
# in increasing orders of magnitude
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
