import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from apps.lostnumber import MyLostNumber

import unittest

class TestMyLostNumber(unittest.TestCase):

    def test_mylostnumber(self):
        myLostNumber = MyLostNumber([4, 1, 2, 2, 5, 1, 4, 3])
        myLostNumber.calculate()
        self.assertListEqual(myLostNumber.get_lost_number(), [5, 3])

if __name__ == '__main__':
    unittest.main()

