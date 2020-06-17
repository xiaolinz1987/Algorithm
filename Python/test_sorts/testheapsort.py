import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from sorts.heapsort import MyHeapSort

import unittest

class TestMyHeapSort(unittest.TestCase):

    def test_myheapsort(self):
        myHeapSort = MyHeapSort([3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11])
        myHeapSort.heap_sort()
        self.assertListEqual(myHeapSort.get_array(), [14, 11, 9, 8, 7, 6, 5, 4, 3, 1, 1, 0, -1])

if __name__ == '__main__':
    unittest.main()

