import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from sorts.cocktailsort import MyCockTailSort

import unittest

class TestMyCockTailSort(unittest.TestCase):

    def test_mycocktailsort(self):
        myCockTailSort = MyCockTailSort([3, 4, 14, 1, 5, 6, 7, 8, 1, -1, 0, 9, 11])
        myCockTailSort.cock_tail_sort()
        self.assertListEqual(myCockTailSort.get_array(), [-1, 0, 1, 1, 3, 4, 5, 6, 7, 8, 9, 11, 14])

if __name__ == '__main__':
    unittest.main()

