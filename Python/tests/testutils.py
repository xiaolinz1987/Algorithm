import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.array import MyArray
from utils.heap import MyHeap
from utils.linkedlist import MyLinkedList
from utils.queue import MyQueue
from utils.tree import MyTree
from utils.priorityqueue import MyPriorityQueue

import unittest

class TestUtils(unittest.TestCase):

    def test_my_array(self):
        array = MyArray(4)
        array.insert_v1(0, 10)
        self.assertListEqual(array.get_array(), [10])
        array.insert_v1(0, 11)
        self.assertListEqual(array.get_array(), [11, 10])
        array.insert_v1(0, 15)
        self.assertListEqual(array.get_array(), [15, 11, 10])
        array.insert_v1(0, 20)
        self.assertListEqual(array.get_array(), [20, 15, 11, 10])
        array.insert_v2(0, 29)
        self.assertListEqual(array.get_array(), [29, 20, 15, 11, 10])
        array.insert_v2(0, 32)
        self.assertListEqual(array.get_array(), [32, 29, 20, 15, 11, 10])
        array.insert_v2(0, 41)
        self.assertListEqual(array.get_array(), [41, 32, 29, 20, 15, 11, 10])
        array.insert_v2(0, 58)
        self.assertListEqual(array.get_array(), [58, 41, 32, 29, 20, 15, 11, 10])
        array.remove(1)
        self.assertListEqual(array.get_array(), [58, 32, 29, 20, 15, 11, 10])

    def test_my_heap(self):
        heap = MyHeap([1, 3, 2, 6, 5, 7, 8, 9, 10, 0])
        heap.up_adjust()
        self.assertListEqual(heap.get_heap(), [0, 1, 2, 6, 3, 7, 8, 9, 10, 5])
        heap.reset_input([7, 1, 3, 10, 5, 2, 8, 9, 6])
        heap.build()
        self.assertListEqual(heap.get_heap(), [1, 5, 2, 6, 7, 3, 8, 9, 10])

    def test_my_linkedlist(self):
        linkedList = MyLinkedList()
        linkedList.insert(3, 0)
        self.assertListEqual(linkedList.get_list(), [3])
        linkedList.insert(4, 0)
        self.assertListEqual(linkedList.get_list(), [4, 3])
        linkedList.insert(9, 2)
        self.assertListEqual(linkedList.get_list(), [4, 3, 9])
        linkedList.insert(5, 3)
        self.assertListEqual(linkedList.get_list(), [4, 3, 9, 5])
        linkedList.insert(6, 1)
        self.assertListEqual(linkedList.get_list(), [4, 6, 3, 9, 5])
        linkedList.remove(0)
        self.assertListEqual(linkedList.get_list(), [6, 3, 9, 5])

    def test_my_queue(self):
        queue = MyQueue(6)
        queue.enqueue(3)
        self.assertListEqual(queue.get_queue(), [3])
        queue.enqueue(5)
        self.assertListEqual(queue.get_queue(), [3, 5])
        queue.enqueue(6)
        self.assertListEqual(queue.get_queue(), [3, 5, 6])
        queue.dequeue()
        self.assertListEqual(queue.get_queue(), [5, 6])
        queue.dequeue()
        self.assertListEqual(queue.get_queue(), [6])
        queue.enqueue(2)
        self.assertListEqual(queue.get_queue(), [6, 2])
        queue.enqueue(4)
        self.assertListEqual(queue.get_queue(), [6, 2, 4])

    def test_my_tree(self):
        tree = MyTree([3, 2, 9, None, None, 10, None, None, 8, None, 4])
        tree.pre_order_traversal()
        self.assertListEqual(tree.get_tree(), [3, 2, 9, 10, 8, 4])
        tree.pre_order_traversal_with_stack()
        self.assertListEqual(tree.get_tree(), [3, 2, 9, 10, 8, 4])
        tree.in_order_traversal()
        self.assertListEqual(tree.get_tree(), [9, 2, 10, 3, 8, 4])
        tree.in_order_traversal_with_stack()
        self.assertListEqual(tree.get_tree(), [9, 2, 10, 3, 8, 4])
        tree.post_order_traversal()
        self.assertListEqual(tree.get_tree(), [9, 10, 2, 4, 8, 3])
        tree.post_order_traversal_with_stack()
        self.assertListEqual(tree.get_tree(), [9, 10, 2, 4, 8, 3])
        tree.level_order_traversal()
        self.assertListEqual(tree.get_tree(), [3, 2, 8, 9, 10, 4])

    def test_my_priorityqueue(self):
        queue = MyPriorityQueue()
        queue.enqueue(3)
        queue.enqueue(5)
        queue.enqueue(10)
        queue.enqueue(2)
        queue.enqueue(7)
        self.assertEqual(queue.dequeue(), 10)
        self.assertEqual(queue.dequeue(), 7)
        self.assertEqual(queue.dequeue(), 5)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 2)

if __name__ == '__main__':
    unittest.main()

