import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from apps.greatestsorteddistance import MyGreatestSortedDistance

import unittest

class TestMyGreatestSortedDistance(unittest.TestCase):

    def test_mygreatestsorteddistance(self):
        myGreatestSortedDistance = MyGreatestSortedDistance([2, 6, 3, 5, 6, 10, 9])
        myGreatestSortedDistance.calcuate()
        self.assertEqual(myGreatestSortedDistance.get_greatest_sorted_distance(), 3)

if __name__ == '__main__':
    unittest.main()

