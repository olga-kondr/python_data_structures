import unittest
from min_heap import MinHeap

class TestMinHeapMethods(unittest.TestCase):

    def test_pop(self):
        heap = MinHeap([2, 4, 9, 15])
        self.assertEqual(heap.pop(), 2)

    def test_pop_empty(self):
        heap = MinHeap([])
        self.assertFalse(heap.pop())

    def test_push_mid_value(self):
        heap = MinHeap([2, 4, 9, 15])
        heap.push(8)
        self.assertEqual(str(heap), str(MinHeap([2, 4, 9, 15, 8])))

    def test_push_min_value(self):
        heap = MinHeap([2, 4, 9, 15, 8])
        heap.push(1)
        self.assertEqual(str(heap), str(MinHeap([1, 4, 2, 15, 8, 9])))

    def test_push_to_empty_heap(self):
        heap = MinHeap([])
        heap.push(7)
        self.assertEqual(str(heap), str(MinHeap([7])))

    def test_peek(self):
        heap = MinHeap([2, 4, 9, 15, 8])
        self.assertEqual(heap.peek(), 2)

    def test_peek_empty_heap(self):
        heap = MinHeap([])
        self.assertFalse(heap.peek())

if __name__ == '__main__':
    unittest.main()

