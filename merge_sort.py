def merge_sort(unord_list):
    return merge_helper(
        unord_list[:(len(unord_list)/2)],
        unord_list[(len(unord_list)/2):]
        )


def merge_helper(left, right):
    """A sorting algorithm that splits an unorderd list in half,
    repeatedly, until it is reduced to individual chunks, then
    sorts the chunks."""
    if len(right) == 1 and len(left) == 1:
        return [min(left[0], right[0]), max(left[0], right[0])]

    if len(right) == 0 or len(left) == 0:
        return right

    left = merge_helper(left[:(len(left)/2)], left[(len(left)/2):])
    right = merge_helper(right[:(len(right)/2)], right[(len(right)/2):])
    l = []
    for var in right:
        while len(left) > 0 and left[0] < var:
            l.append(left.pop(0))
        l.append(var)
    l += left
    return l


if __name__ == "__main__":
    from time import time

    def worst_case(num):
        left = []
        right = []
        put_in_left = True
        for i in range(num):
            if put_in_left:
                left.append(i)
            else:
                right.append(i)
            put_in_left = not put_in_left
        left += right

        timer = time()
        merge_sort(left)
        return time() - timer

    def best_case(num):
        l = range(num)
        timer = time()
        merge_sort(l)
        return time() - timer

    print "worst case: "+str(worst_case(100000))
    print "best case: "+str(best_case(100000))
