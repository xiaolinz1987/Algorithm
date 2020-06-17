import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from apps.bestgoldmining import MyBestGoldMining

import unittest

class TestMyBestGoldMining(unittest.TestCase):

    def test_mybestgoldmining(self):
        workers = 10
        mines = 5
        mining_workers = list([5, 5, 3, 4, 3])
        mining_amount = list([400, 500, 200, 300, 350])
        myBestGoldMining = MyBestGoldMining(workers, mines, mining_workers, mining_amount)
        myBestGoldMining.mining_v1()
        self.assertEqual(myBestGoldMining.get_mining(), 900)
        myBestGoldMining.reset(workers, mines, mining_workers, mining_amount)
        myBestGoldMining.mining_v2()
        self.assertEqual(myBestGoldMining.get_mining(), 900)
        myBestGoldMining.reset(workers, mines, mining_workers, mining_amount)
        myBestGoldMining.mining_v3()
        self.assertEqual(myBestGoldMining.get_mining(), 900)

if __name__ == '__main__':
    unittest.main()

