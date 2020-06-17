import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from apps.greatestcommondivisor import MyGreatestCommonDivisor

import unittest

class TestMyGreatestCommonDivisor(unittest.TestCase):
    
    def test_mygreatestcommondivisor(self):
        myGreatestCommonDivisor = MyGreatestCommonDivisor(25, 5)
        myGreatestCommonDivisor.calculate_v1()
        self.assertEqual(myGreatestCommonDivisor.get_greatest_common_divisor(), 5)
        myGreatestCommonDivisor.set(100, 75)
        myGreatestCommonDivisor.calculate_v2()
        self.assertEqual(myGreatestCommonDivisor.get_greatest_common_divisor(), 25)
        myGreatestCommonDivisor.set(99, 55)
        myGreatestCommonDivisor.calculate_v3()
        self.assertEqual(myGreatestCommonDivisor.get_greatest_common_divisor(), 11)
        myGreatestCommonDivisor.set(10000, 1)
        myGreatestCommonDivisor.calculate_v4()
        self.assertEqual(myGreatestCommonDivisor.get_greatest_common_divisor(), 1)
        myGreatestCommonDivisor.set(10000, 10001)
        myGreatestCommonDivisor.calculate_v4()
        self.assertEqual(myGreatestCommonDivisor.get_greatest_common_divisor(), 1)

if __name__ == '__main__':
    unittest.main()

