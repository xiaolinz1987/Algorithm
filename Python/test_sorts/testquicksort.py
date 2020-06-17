import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from sorts.quicksort import MyQuickSort

import unittest

class TestMyQuickSort(unittest.TestCase):

    def test_myquicksort(self):
        inputArray = list([3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11])
        expectedArray = list([-1, 0, 1, 1, 3, 4, 5, 6, 7, 8, 9, 11, 14])

        myQuickSort = MyQuickSort(inputArray)
        myQuickSort.quick_sort_v1()
        self.assertListEqual(myQuickSort.get_array(), expectedArray)
        myQuickSort.reset_input(inputArray)
        myQuickSort.quick_sort_v2()
        self.assertListEqual(myQuickSort.get_array(), expectedArray)
        myQuickSort.reset_input(inputArray)
        myQuickSort.quick_sort_v3()
        self.assertListEqual(myQuickSort.get_array(), expectedArray)

if __name__ == '__main__':
    unittest.main()

