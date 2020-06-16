import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.linkedlist import MyLinkedList

import unittest

class TestMyLinkedList(unittest.TestCase):

    def test_mylinkedlist(self):
        myLinkedList = MyLinkedList()
        myLinkedList.insert(3, 0)
        self.assertListEqual(myLinkedList.get_list(), [3])
        myLinkedList.insert(4, 0)
        self.assertListEqual(myLinkedList.get_list(), [4, 3])
        myLinkedList.insert(9, 2)
        self.assertListEqual(myLinkedList.get_list(), [4, 3, 9])
        myLinkedList.insert(5, 3)
        self.assertListEqual(myLinkedList.get_list(), [4, 3, 9, 5])
        myLinkedList.insert(6, 1)
        self.assertListEqual(myLinkedList.get_list(), [4, 6, 3, 9, 5])
        myLinkedList.remove(0)
        self.assertListEqual(myLinkedList.get_list(), [6, 3, 9, 5])

if __name__ == '__main__':
    unittest.main()
