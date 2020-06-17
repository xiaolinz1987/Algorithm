import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from projects.redpackage import MyRedPackage

import unittest

class TestMyRedPackage(unittest.TestCase):

    def test_myredpackage(self):
        myRedPackage = MyRedPackage(1000, 10)
        myRedPackage.divide()
        for package in myRedPackage.get_packages():
            self.assertLess(package, 220)
            self.assertGreater(package, 1)

if __name__ == '__main__':
    unittest.main()

