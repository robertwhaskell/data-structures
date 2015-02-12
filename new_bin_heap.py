class Heap:
    def __init__(self):
        self.heapList = []
        self.size = 0

    def push(self, val):
        self.heapList.append(val)
        self.size += 1
        self.sort_up(self.size)

    def sort_up(self, i):
        while (i-1) // 2 > 0:
            # this line will need altered to handle user spec
            if self.heapList[i] > self.heapList[(i-1) // 2]:
                temp = self.heapList[(i - 1) // 2]
                self.heapList[(i-1) // 2] = self.heapList[i]
                self.heapList[i] = temp
            i = (i - 1) // 2
