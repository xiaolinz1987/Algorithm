import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.tree import MyTree

import unittest

class TestMyTree(unittest.TestCase):

    def test_mytree(self):
        myTree = MyTree([3, 2, 9, None, None, 10, None, None, 8, None, 4])
        myTree.pre_order_traversal()
        self.assertListEqual(myTree.get_tree(), [3, 2, 9, 10, 8, 4])
        myTree.pre_order_traversal_with_stack()
        self.assertListEqual(myTree.get_tree(), [3, 2, 9, 10, 8, 4])
        myTree.in_order_traversal()
        self.assertListEqual(myTree.get_tree(), [9, 2, 10, 3, 8, 4])
        myTree.in_order_traversal_with_stack()
        self.assertListEqual(myTree.get_tree(), [9, 2, 10, 3, 8, 4])
        myTree.post_order_traversal()
        self.assertListEqual(myTree.get_tree(), [9, 10, 2, 4, 8, 3])
        myTree.post_order_traversal_with_stack()
        self.assertListEqual(myTree.get_tree(), [9, 10, 2, 4, 8, 3])
        myTree.level_order_traversal()
        self.assertListEqual(myTree.get_tree(), [3, 2, 8, 9, 10, 4])

if __name__ == '__main__':
    unittest.main()
