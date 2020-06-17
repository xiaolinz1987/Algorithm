import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.linkedlist import Node
from apps.cyclelist import MyCycleList

import unittest

class TestMyCycleList(unittest.TestCase):

    def test_mycyclelist(self):
        node1 = Node(5)
        node2 = Node(3)
        node3 = Node(7)
        node4 = Node(2)
        node5 = Node(6)
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node5
        node5.next = node2

        myCycleList = MyCycleList(node1)
        myCycleList.check_cycle()
        myCycleList.check_cycle_length()
        myCycleList.check_cycle_start()
        self.assertEqual(myCycleList.get_cycle_length(), 4)
        self.assertEqual(myCycleList.get_cycle_start(), 3)

if __name__ == '__main__':
    unittest.main()

