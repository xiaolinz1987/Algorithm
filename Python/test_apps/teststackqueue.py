import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from apps.stackqueue import MyStackQueue

import unittest

class TestMyStackQueue(unittest.TestCase):

    def test_mystackqueue(self):
        myStackQueue = MyStackQueue()
        myStackQueue.enqueue(1)
        myStackQueue.enqueue(2)
        myStackQueue.enqueue(3)
        self.assertEqual(myStackQueue.dequeue(), 1)
        self.assertEqual(myStackQueue.dequeue(), 2)
        myStackQueue.enqueue(4)
        self.assertEqual(myStackQueue.dequeue(), 3)
        self.assertEqual(myStackQueue.dequeue(), 4)

if __name__ == '__main__':
    unittest.main()

