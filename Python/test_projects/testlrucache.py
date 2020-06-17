import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from projects.lrucache import MyLRUCache

import unittest

class TestMyLRUCache(unittest.TestCase):

    def test_mylrucache(self):
        myLRUCache = MyLRUCache(5)
        myLRUCache.put("001", "User1")
        self.assertEqual(myLRUCache.get("001"), "User1")
        myLRUCache.put("002", "User2")
        myLRUCache.put("003", "User3")
        myLRUCache.put("004", "User4")
        myLRUCache.put("005", "User5")
        self.assertEqual(myLRUCache.get("002"), "User2")
        myLRUCache.put("004", "User4 update")
        myLRUCache.put("006", "User6")
        self.assertIsNone(myLRUCache.get("001"))
        self.assertEqual(myLRUCache.get("006"), "User6")

if __name__ == '__main__':
    unittest.main()

