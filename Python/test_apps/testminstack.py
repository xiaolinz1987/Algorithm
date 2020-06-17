import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from apps.minstack import MyMinStack

import unittest

class TestMyMinStack(unittest.TestCase):

    def test_myminstack(self):
        myMinStack = MyMinStack()
        myMinStack.push(4)
        myMinStack.push(9)
        myMinStack.push(7)
        myMinStack.push(3)
        myMinStack.push(8)
        myMinStack.push(5)
        self.assertEqual(myMinStack.get_min(), 3)
        myMinStack.pop()
        myMinStack.pop()
        myMinStack.pop()
        self.assertEqual(myMinStack.get_min(), 4)

if __name__ == '__main__':
    unittest.main()

