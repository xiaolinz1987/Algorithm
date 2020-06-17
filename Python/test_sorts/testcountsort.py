import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from sorts.countsort import MyCountSort

import unittest

class TestMyCountSort(unittest.TestCase):

    def test_mycountsort(self):
        myCountSort = MyCountSort([4, 4, 6, 5, 3, 2, 8, 1, 7, 5, 6, 0, 10])
        myCountSort.count_sort_v1()
        self.assertListEqual(myCountSort.get_array(), [0, 1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 8, 10])
        myCountSort.reset([95, 94, 91, 98, 99, 90, 99, 93, 91, 92])
        myCountSort.count_sort_v2()
        self.assertListEqual(myCountSort.get_array(), [90, 91, 91, 92, 93, 94, 95, 98, 99, 99])

if __name__ == '__main__':
    unittest.main()

