import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from utils.linkedlist import Node
from apps.bestgoldmining import MyBestGoldMining
from apps.cyclelist import MyCycleList
from apps.dictionarysort import MyDictionarySort
from apps.greatestcommondivisor import MyGreatestCommonDivisor
from apps.greatestsorteddistance import MyGreatestSortedDistance
from apps.lostnumber import MyLostNumber
from apps.mediansortedarrays import MyMedianSortedArrays
from apps.minstack import MyMinStack
from apps.removekdigits import MyRemoveKDigits
from apps.stackqueue import MyStackQueue

import unittest

class TestApps(unittest.TestCase):

    def test_my_bestgoldmining(self):
        workers = 10
        mines = 5
        mining_workers = list([5, 5, 3, 4, 3])
        mining_amount = list([400, 500, 200, 300, 350])
        mining = MyBestGoldMining(workers, mines, mining_workers, mining_amount)
        mining.mining_v1()
        self.assertEqual(mining.get_mining(), 900)
        mining.reset(workers, mines, mining_workers, mining_amount)
        mining.mining_v2()
        self.assertEqual(mining.get_mining(), 900)
        mining.reset(workers, mines, mining_workers, mining_amount)
        mining.mining_v3()
        self.assertEqual(mining.get_mining(), 900)

    def test_my_cyclelist(self):
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

        cycleList = MyCycleList(node1)
        cycleList.check_cycle()
        cycleList.check_cycle_length()
        cycleList.check_cycle_start()
        self.assertEqual(cycleList.get_cycle_length(), 4)
        self.assertEqual(cycleList.get_cycle_start(), 3)

    def test_my_dictionarysort(self):
        dictSort = MyDictionarySort([1, 2, 3, 4, 5])
        dictSort.sort()
        self.assertListEqual(dictSort.get_array(), [1, 2, 3, 5, 4])
        dictSort.reset([1, 3, 4, 5, 2])
        dictSort.sort()
        self.assertListEqual(dictSort.get_array(), [1, 3, 5, 2, 4])

    def test_my_greatestcommondivisor(self):
        divisor = MyGreatestCommonDivisor(25, 5)
        divisor.calculate_v1()
        self.assertEqual(divisor.get_greatest_common_divisor(), 5)
        divisor.set(100, 75)
        divisor.calculate_v2()
        self.assertEqual(divisor.get_greatest_common_divisor(), 25)
        divisor.set(99, 55)
        divisor.calculate_v3()
        self.assertEqual(divisor.get_greatest_common_divisor(), 11)
        divisor.set(10000, 1)
        divisor.calculate_v4()
        self.assertEqual(divisor.get_greatest_common_divisor(), 1)
        divisor.set(10000, 10001)
        divisor.calculate_v4()
        self.assertEqual(divisor.get_greatest_common_divisor(), 1)

    def test_my_greatestsorteddistance(self):
        distance = MyGreatestSortedDistance([2, 6, 3, 5, 6, 10, 9])
        distance.calcuate()
        self.assertEqual(distance.get_greatest_sorted_distance(), 3)

    def test_my_lost_number(self):
        lost = MyLostNumber([4, 1, 2, 2, 5, 1, 4, 3])
        lost.calculate()
        self.assertListEqual(lost.get_lost_number(), [5, 3])

    def test_my_mediansortedarrays(self):
        median = MyMedianSortedArrays([3, 5, 6, 7, 8, 12, 20],
                                        [1, 10, 17, 18])
        median.calculate()
        self.assertEqual(median.get_median(), 8)

    def test_my_minstack(self):
        minStack = MyMinStack()
        minStack.push(4)
        minStack.push(9)
        minStack.push(7)
        minStack.push(3)
        minStack.push(8)
        minStack.push(5)
        self.assertEqual(minStack.get_min(), 3)
        minStack.pop()
        minStack.pop()
        minStack.pop()
        self.assertEqual(minStack.get_min(), 4)

    def test_my_removekdigits(self):
        digits = MyRemoveKDigits("1593212", 3)
        digits.remove_v1()
        self.assertEqual(digits.get_digits(), "1212")
        digits.reset("30200", 1)
        digits.remove_v1()
        self.assertEqual(digits.get_digits(), "200")
        digits.reset("10", 2)
        digits.remove_v1()
        self.assertEqual(digits.get_digits(), "0")
        digits.reset("1593212", 3)
        digits.remove_v2()
        self.assertEqual(digits.get_digits(), "1212")

    def test_my_stackqueue(self):
        queue = MyStackQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        queue.enqueue(4)
        self.assertEqual(queue.dequeue(), 3)
        self.assertEqual(queue.dequeue(), 4)

if __name__ == '__main__':
    unittest.main()

