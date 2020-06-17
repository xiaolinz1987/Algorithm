import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from sorts.bubblesort import MyBubbleSort

import unittest

class TestMyBubbleSort(unittest.TestCase):

    def test_mybubblesort(self):
        inputArray = list([3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11])
        sortedArray = list([-1, 0, 1, 1, 3, 4, 5, 6, 7, 8, 9, 11, 14])
        
        myBubbleSort = MyBubbleSort(inputArray)
        myBubbleSort.bubble_sort_v1()
        self.assertListEqual(myBubbleSort.get_array(), sortedArray)
        myBubbleSort.reset_input(inputArray)
        myBubbleSort.bubble_sort_v2()
        self.assertListEqual(myBubbleSort.get_array(), sortedArray)
        myBubbleSort.bubble_sort_v3()
        self.assertListEqual(myBubbleSort.get_array(), sortedArray)

if __name__ == '__main__':
    unittest.main()
