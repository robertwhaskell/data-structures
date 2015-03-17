def merge_sort(unord_list):
    pass


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
