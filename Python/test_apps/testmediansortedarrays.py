import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from apps.mediansortedarrays import MyMedianSortedArray

import unittest

class TestMyMedianSortedArrays(unittest.TestCase):

    def test_mymediansortedarrays(self):
        myMedianSortedArrays = MyMedianSortedArray([3, 5, 6, 7, 8, 12, 20],
                                                [1, 10, 17, 18])
        myMedianSortedArrays.calculate()
        self.assertEqual(myMedianSortedArrays.get_median(), 8)

if __name__ == '__main__':
    unittest.main()

