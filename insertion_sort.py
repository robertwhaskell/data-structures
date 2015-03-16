def insertion_sort(unordered_list):
    # inspect the first value in the list.
    # if that value if larger than the next value in the list,
    # swap them. If not, leave it be.
    for i in len(unordered_list):
        try:
            moving = i + 1
            while (unordered_list[moving] < unordered_list[moving - 1]):
                unordered_list[moving], unordered_list[moving - 1] = unordered_list[moving - 1], unordered_list[moving]
                if moving > 1:
                    moving -= 1
                else:
                    break
        except IndexError:
            return unordered_list


if __name__ == "__main__":
    from random import sample
    random_list = sample(range(1000), 1000)
    pass