import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from apps.removekdigits import MyRemoveKDigits

import unittest

class TestMyRemoveKDigits(unittest.TestCase):

    def test_myremovekdigits(self):
        myRemoveKDigits = MyRemoveKDigits("1593212", 3)
        myRemoveKDigits.remove_v1()
        self.assertEqual(myRemoveKDigits.get_digits(), "1212")
        myRemoveKDigits.reset("30200", 1)
        myRemoveKDigits.remove_v1()
        self.assertEqual(myRemoveKDigits.get_digits(), "200")
        myRemoveKDigits.reset("10", 2)
        myRemoveKDigits.remove_v1()
        self.assertEqual(myRemoveKDigits.get_digits(), "0")
        myRemoveKDigits.reset("1593212", 3)
        myRemoveKDigits.remove_v2()
        self.assertEqual(myRemoveKDigits.get_digits(), "1212")

if __name__ == '__main__':
    unittest.main()

