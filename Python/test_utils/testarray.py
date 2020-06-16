import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.array import MyArray

import unittest

class TestMyArray(unittest.TestCase):

    def test_myarray(self):
        myArray = MyArray(4)
        myArray.insert_v1(0, 10)
        self.assertListEqual(myArray.get_array(), [10])
        myArray.insert_v1(0, 11)
        self.assertListEqual(myArray.get_array(), [11, 10])
        myArray.insert_v1(0, 15)
        self.assertListEqual(myArray.get_array(), [15, 11, 10])
        myArray.insert_v1(0, 20)
        self.assertListEqual(myArray.get_array(), [20, 15, 11, 10])
        myArray.insert_v2(0, 29)
        self.assertListEqual(myArray.get_array(), [29, 20, 15, 11, 10])
        myArray.insert_v2(0, 32)
        self.assertListEqual(myArray.get_array(), [32, 29, 20, 15, 11, 10])
        myArray.insert_v2(0, 41)
        self.assertListEqual(myArray.get_array(), [41, 32, 29, 20, 15, 11, 10])
        myArray.insert_v2(0, 58)
        self.assertListEqual(myArray.get_array(), [58, 41, 32, 29, 20, 15, 11, 10])
        myArray.remove(1)
        self.assertListEqual(myArray.get_array(), [58, 32, 29, 20, 15, 11, 10])

if __name__ == '__main__':
    unittest.main()
