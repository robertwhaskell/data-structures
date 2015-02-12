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

    def pop(self):
        val = self.heapList[0]
        self.heapList[0] = self.heapList[self.size -1]
        self.size -= 1
        self.heapList.pop()
        self.sort_down(0)

    def sort_down(self, i):
        while ((i + 1) * 2) <= self.size:
            max_child = self.maxChild(i)
            if self.heapList[i] < self.heapList[max_child]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[max_child]
                self.heapList[max_child] = temp
            i = max_child

    def maxChild(self, i):
        if (i * 2 + 2) > self.size:
            return (i * 2 + 1)
        else:
            if self.heapList[i*2 + 1] > self.heapList[i * 2 + 2]:
                return (i * 2 + 1)
            else:
                return (i * 2 + 2)
