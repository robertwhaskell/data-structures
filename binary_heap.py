class Heap(object):
    def __init__(self, new_list=[]):
        self.heap_list = [0]
        self.heap_list += new_list
        self.head = self.heap_list[0]

    def push(self, val):
        self.heap_list.append(val)
        self.sort_up(len(self.heap_list) - 1)

    def pop(self):
        try:
            self.heap_list[1] = self.heap_list.pop()
            self.sort_down(1)
        except IndexError:
            raise IndexError("List empty")

    def sort_down(self, index):
        while (index * 2) > (len(self.heap_list) - 1):
            max_child = self.max_child(index)
            if self.heap_list[max_child] > self.heap_list[index]:
                temp = self.heap_list[index]
                self.heap_list[index] = self.heap_list[max_child]
                self.heap_list[max_child] = temp
            index = max_child

    def sort_up(self, index):
        while self.heap_list[index] > self.heap_list[index // 2]:
            if index == 1:
                break
            temp = self.heap_list[index]
            self.heap_list[index] = self.heap_list[index // 2]
            self.heap_list[index // 2] = temp
            index = index // 2

    def max_child(self, index):
        if (index * 2 + 1) > (len(self.heap_list) - 1):
            return (index * 2)
        if self.heap_list[index * 2] > self.heap_list[index * 2 + 1]:
            return (index * 2)
        return (index * 2 + 1)
