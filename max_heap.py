class MaxHeap:
    def __init__(self, items=[]):
        super().__init__()
        self.heap = [0]

        for each in items:
            self.heap.append(each)
            self.__move_up(len(self.heap) - 1)

    def push(self, item):
        self.heap.append(item)
        self.__move_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) > 2:
            self.__swap(1, len(self.heap) - 1)
            max_item = self.heap.pop()
            self.__move_down(1)
        elif len(self.heap) == 2:
            max_item = self.heap.pop()
        else:
            max_item = False
        return max_item

    def peek(self):
        if self.heap[1]:
            return self.heap[1]
        else:
            return False

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def __move_up(self, ind):
        parent = ind//2
        if ind <=1:
            return
        elif self.heap[ind] > self.heap[parent]:
            self.__swap(ind, parent)
            self.__move_up(parent) 

    def __move_down(self, ind):
        left = ind * 2
        right = ind * 2 + 1
        big = ind

        if len(self.heap) > left and self.heap[big] < self.heap[left]:
            big = left
        if len(self.heap) > right and self.heap[big] < self.heap[right]:
            big = right
        if big != ind:
            self.__swap(ind, big)
            self.__move_down(big)
            
    def __str__(self):
        return str(self.heap)


if __name__ == "__main__":
    heap = MaxHeap([15, 4, 9, 1])
    heap.push(8)
    print(heap)
    heap.pop()
    print(heap.peek())
    print(heap)
    heap.push(100)
    print(heap)
