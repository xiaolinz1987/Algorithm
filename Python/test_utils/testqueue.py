import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.queue import MyQueue

import unittest

class TestMyQueue(unittest.TestCase):

    def test_myqueue(self):
        myQueue = MyQueue(6)
        myQueue.enqueue(3)
        self.assertListEqual(myQueue.get_queue(), [3])
        myQueue.enqueue(5)
        self.assertListEqual(myQueue.get_queue(), [3, 5])
        myQueue.enqueue(6)
        self.assertListEqual(myQueue.get_queue(), [3, 5, 6])
        myQueue.dequeue()
        self.assertListEqual(myQueue.get_queue(), [5, 6])
        myQueue.dequeue()
        self.assertListEqual(myQueue.get_queue(), [6])
        myQueue.enqueue(2)
        self.assertListEqual(myQueue.get_queue(), [6, 2])
        myQueue.enqueue(4)
        self.assertListEqual(myQueue.get_queue(), [6, 2, 4])

if __name__ == '__main__':
    unittest.main()
