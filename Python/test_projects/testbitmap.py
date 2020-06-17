import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from projects.bitmap import MyBitmap

import unittest

class TestMyBitmap(unittest.TestCase):

    def test_mybitmap(self):
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
        if word_size_1 > word_size_2:
            for i in range(word_size, word_size_1):
                union[i] = bit1.words[i]
        else:
            for i in range(word_size, word_size_2):
                union[i] = bit2.words[i]
        self.assertListEqual(union, [14])

if __name__ == '__main__':
    unittest.main()
