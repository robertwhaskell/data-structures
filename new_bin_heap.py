class Heap:
    def __init__(self, new_list=None):
        self.heapList = [0]  # root 0 simplifies math
        self.size = 0
        if new_list:
            i = len(new_list) // 2
            self.size = len(new_list)
            self.heapList += new_list[:]
            while (i > 0):
                self.sort_down(i)
                i -= 1

    def push(self, val):
        self.heapList.append(val)
        self.size += 1
        self.sort_up(self.size)

    def sort_up(self, i):
        while i // 2 > 0:
            # this line will need altered to handle user spec
            if self.heapList[i] > self.heapList[i // 2]:
                temp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = temp
            i = i // 2

    def pop(self):
        val = self.heapList[1]
        self.heapList[1] = self.heapList[self.size]
        self.size -= 1
        self.heapList.pop()
        self.sort_down(1)
        return val

    def sort_down(self, i):
        while (i * 2) <= self.size:
            max_child = self.maxChild(i)
            # user spec change
            if self.heapList[i] < self.heapList[max_child]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[max_child]
                self.heapList[max_child] = temp
            i = max_child

    def maxChild(self, i):
        if (i * 2 + 1) > self.size:
            return (i * 2)
        # user spec change
        if self.heapList[i * 2] > self.heapList[i * 2 + 1]:
            return (i * 2)
        return (i * 2 + 1)
