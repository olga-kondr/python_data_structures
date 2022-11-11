import unittest
from max_heap import MaxHeap

class TestMaxHeapMethods(unittest.TestCase):

    def test_pop(self):
        heap = MaxHeap([15, 4, 9, 1])
        self.assertEqual(heap.pop(), 15)

    def test_pop_empty(self):
        heap = MaxHeap([])
        self.assertFalse(heap.pop())

    def test_push(self):
        heap = MaxHeap([15, 4, 9, 1])
        heap.push(8)
        self.assertEqual(str(heap), str(MaxHeap([15, 8, 9, 1, 4])))
    
    def test_push_max_value(self):
        heap = MaxHeap([15, 4, 9, 1])
        heap.push(20)
        self.assertEqual(str(heap), str(MaxHeap([20, 15, 9, 1, 4])))

    def test_push_to_empty_heap(self):
        heap = MaxHeap([])
        heap.push(7)
        self.assertEqual(str(heap), str(MaxHeap([7])))

    def test_peek(self):
        heap = MaxHeap([15, 4, 9, 1])
        self.assertEqual(heap.peek(), 15)

    def test_peek_empty_heap(self):
        heap = MaxHeap([])
        self.assertFalse(heap.peek())

if __name__ == '__main__':
    unittest.main()

