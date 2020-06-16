import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.priorityqueue import MyPriorityQueue

import unittest

class TestMyPriorityQueue(unittest.TestCase):

    def test_mypriorityqueue(self):
        myQueue = MyPriorityQueue()
        myQueue.enqueue(3)
        myQueue.enqueue(5)
        myQueue.enqueue(10)
        myQueue.enqueue(2)
        myQueue.enqueue(7)
        self.assertEqual(myQueue.dequeue(), 10)
        self.assertEqual(myQueue.dequeue(), 7)
        self.assertEqual(myQueue.dequeue(), 5)
        self.assertEqual(myQueue.dequeue(), 3)
        self.assertEqual(myQueue.dequeue(), 2)

if __name__ == '__main__':
    unittest.main()
