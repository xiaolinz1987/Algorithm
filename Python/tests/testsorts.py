import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from sorts.bubblesort import MyBubbleSort
from sorts.bucketsort import MyBucketSort
from sorts.cocktailsort import MyCockTailSort
from sorts.quicksort import MyQuickSort
from sorts.countsort import MyCountSort
from sorts.heapsort import MyHeapSort

import unittest

class TestSorts(unittest.TestCase):

    def test_my_bubblesort(self):
        input = list([3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11])
        sorted = list([-1, 0, 1, 1, 3, 4, 5, 6, 7, 8, 9, 11, 14])
        
        bubbleSort = MyBubbleSort(input)
        bubbleSort.bubble_sort_v1()
        self.assertListEqual(bubbleSort.get_array(), sorted)
        bubbleSort.reset_input(input)
        bubbleSort.bubble_sort_v2()
        self.assertListEqual(bubbleSort.get_array(), sorted)
        bubbleSort.reset_input(input)
        bubbleSort.bubble_sort_v3()
        self.assertListEqual(bubbleSort.get_array(), sorted)

    def test_my_bucketsort(self):
        bucketSort = MyBucketSort([4.12, 6.421, 0.0023, 3.0, 2.123, 8.122, 4.12, 10.09])
        bucketSort.bucket_sort()
        self.assertListEqual(bucketSort.get_array(), [0.0023, 2.123, 3.0, 4.12, 4.12, 6.421, 8.122, 10.09])

    def test_my_cocktailsort(self):
        cocktailSort = MyCockTailSort([3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11])
        cocktailSort.cock_tail_sort()
        self.assertListEqual(cocktailSort.get_array(), [-1, 0, 1, 1, 3, 4, 5, 6, 7, 8, 9, 11, 14])

    def test_my_quicksort(self):
        input = list([3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11])
        sorted = list([-1, 0, 1, 1, 3, 4, 5, 6, 7, 8, 9, 11, 14])

        quickSort = MyQuickSort(input)
        quickSort.quick_sort_v1()
        self.assertListEqual(quickSort.get_array(), sorted)
        quickSort.reset_input(input)
        quickSort.quick_sort_v2()
        self.assertListEqual(quickSort.get_array(), sorted)
        quickSort.reset_input(input)
        quickSort.quick_sort_v3()
        self.assertListEqual(quickSort.get_array(), sorted)

    def test_my_countsort(self):
        countSort = MyCountSort([4, 4, 6, 5, 3, 2, 8, 1, 7, 5, 6, 0, 10])
        countSort.count_sort_v1()
        self.assertListEqual(countSort.get_array(), [0, 1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 8, 10])
        countSort.reset([95, 94, 91, 98, 99, 90, 99, 93, 91, 92])
        countSort.count_sort_v2()
        self.assertListEqual(countSort.get_array(), [90, 91, 91, 92, 93, 94, 95, 98, 99, 99])

    def test_my_heapsort(self):
        heapSort = MyHeapSort([3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11])
        heapSort.heap_sort()
        self.assertListEqual(heapSort.get_array(), [14, 11, 9, 8, 7, 6, 5, 4, 3, 1, 1, 0, -1])

if __name__ == '__main__':
    unittest.main()

