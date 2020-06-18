import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from projects.bitmap import MyBitmap
from projects.lrucache import MyLRUCache
from projects.astarsearch import MAZE
from projects.astarsearch import Grid
from projects.astarsearch import MyAStarSearch
from projects.redpackage import MyRedPackage

import unittest

class TestProjects(unittest.TestCase):

    def test_my_bitmap(self):
        bit1 = MyBitmap(128)
        bit1.set_bit(126)
        bit1.set_bit(75)
        self.assertTrue(bit1.get_bit(126))
        self.assertTrue(bit1.get_bit(75))
        self.assertFalse(bit1.get_bit(112))
        
        bit1.reset(10)
        bit1.set_bit(1)
        bit1.set_bit(2)
        bit2 = MyBitmap(10)
        bit2.set_bit(1)
        bit2.set_bit(3)

        word_size_1 = bit1.get_word_size()
        word_size_2 = bit2.get_word_size()
        word_size = min(word_size_1, word_size_2)

        intersection = [0] * word_size
        for i in range(0, word_size):
            intersection[i] = bit1.words[i] & bit2.words[i]
        self.assertListEqual(intersection, [2])

        union = [0] * word_size
        for i in range(0, word_size):
            union[i] = bit1.words[i] | bit2.words[i]
        if word_size_1 > word_size:
            for i in range(word_size, word_size_1):
                union[i] = bit1.words[i]
        else:
            for i in range(word_size, word_size_2):
                union[i] = bit2.words[i]
        self.assertListEqual(union, [14])

    def test_my_lrucache(self):
        lru = MyLRUCache(5)
        lru.put("001", "user1")
        self.assertEqual(lru.get("001"), "user1")
        lru.put("002", "user2")
        lru.put("003", "user3")
        lru.put("004", "user4")
        lru.put("005", "user5")
        self.assertEqual(lru.get("002"), "user2")
        lru.put("004", "user4 update")
        lru.put("006", "user6")
        self.assertIsNone(lru.get("001"))
        self.assertEqual(lru.get("006"), "user6")

    def test_my_astarsearch(self):
        start = Grid(2, 1)
        end = Grid(2, 5)
        astar = MyAStarSearch(start, end)
        result = astar.a_star_search()

        path = []
        while result is not None:
            path.append(Grid(result.x, result.y))
            result = result.parent

        result_dict = {}
        index = 0
        for i in range(0, len(MAZE)):
            for j in range(0, len(MAZE[0])):
                if astar.contain_grid(path, i, j):
                    result_dict[index] = (i, j)
                    index += 1

        self.assertDictEqual(result_dict, {0: (0, 2),
            1: (0, 3), 2: (0, 4), 3: (0, 5), 4: (1, 2),
            5: (1, 5), 6: (2, 1), 7: (2, 2), 8: (2, 5)})

    def test_my_redpackage(self):
        redpack = MyRedPackage(1000, 10)
        redpack.divide()
        for package in redpack.get_packages():
            self.assertLess(package, 250)
            self.assertGreater(package, 1)

if __name__ == '__main__':
    unittest.main()

