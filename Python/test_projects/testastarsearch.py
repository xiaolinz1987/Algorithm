import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from projects.astarsearch import MAZE
from projects.astarsearch import Grid
from projects.astarsearch import MyAStarSearch

import unittest

class TestMyAStarSearch(unittest.TestCase):

    def test_myastarsearch(self):
        start = Grid(2, 1)
        end = Grid(2, 5)

        myAStarSearch = MyAStarSearch(start, end)
        result = myAStarSearch.a_star_search()

        path = []
        while result is not None:
            path.append(Grid(result.x, result.y))
            result = result.parent
        
        result_dict = {}
        index = 0
        for i in range(0, len(MAZE)):
            for j in range(0, len(MAZE[0])):
                if myAStarSearch.contain_grid(path, i, j):
                    result_dict[index] = (i, j)
                    index += 1
        
        self.assertDictEqual(result_dict, {0: (0, 2),
                                           1: (0, 3),
                                           2: (0, 4), 
                                           3: (0, 5), 
                                           4: (1, 2), 
                                           5: (1, 5), 
                                           6: (2, 1), 
                                           7: (2, 2), 
                                           8: (2, 5)})
        
if __name__ == '__main__':
    unittest.main()
