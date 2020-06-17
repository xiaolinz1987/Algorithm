import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from sorts.bucketsort import MyBucketSort

import unittest

class TestMyBucketSort(unittest.TestCase):

    def test_mybucketsort(self):
        myBucketSort = MyBucketSort([4.12, 6.421, 0.0023, 3.0, 2.123, 8.122, 4.12, 10.09])
        myBucketSort.bucket_sort()
        self.assertListEqual(myBucketSort.get_array(), [0.0023, 2.123, 3.0, 4.12, 4.12, 6.421, 8.122, 10.09])

if __name__ == '__main__':
    unittest.main()
