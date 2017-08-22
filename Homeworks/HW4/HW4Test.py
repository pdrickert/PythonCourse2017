import unittest
from HW4Rickert import *

class SortTest(unittest.TestCase):

    def test_BubbleSort(self):
        self.assertEqual(BubbleSort([8,6,7,5,3,0,9]), [0,3,5,6,7,8,9])
    def test_SelectionSort(self):
        self.assertEqual(selectionSort([8,6,7,5,3,0,9]), [0,3,5,6,7,8,9])

if __name__ == '__main__':
        unittest.main()
