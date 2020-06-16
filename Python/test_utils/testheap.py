import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.heap import MyHeap

import unittest

class TestMyHeap(unittest.TestCase):

    def test_myheap(self):
        myHeap = MyHeap([1, 3, 2, 6, 5, 7, 8, 9, 10, 0])
        myHeap.up_adjust()
        self.assertListEqual(myHeap.get_heap(), [0, 1, 2, 6, 3, 7, 8, 9, 10, 5])
        myHeap.reset_input([7, 1, 3, 10, 5, 2, 8, 9, 6])
        myHeap.build()
        self.assertListEqual(myHeap.get_heap(), [1, 5, 2, 6, 7, 3, 8, 9, 10])

if __name__ == '__main__':
    unittest.main()
