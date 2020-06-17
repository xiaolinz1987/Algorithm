import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from apps.dictionarysort import MyDictionarySort

import unittest

class TestMyDictionarySort(unittest.TestCase):

    def test_mydictionarysort(self):
        myDictionarySort = MyDictionarySort([1, 2, 3, 4, 5])
        myDictionarySort.sort()
        self.assertListEqual(myDictionarySort.get_array(), [1, 2, 3, 5, 4])
        myDictionarySort.reset([1, 3, 4, 5, 2])
        myDictionarySort.sort()
        self.assertListEqual(myDictionarySort.get_array(), [1, 3, 5, 2, 4])

if __name__ == '__main__':
    unittest.main()

