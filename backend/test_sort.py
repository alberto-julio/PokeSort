import unittest
import sort

class Testing(unittest.TestCase):
    def test_quick_sort(self):
        self.assertEqual(sort.quick_sort([6,5,4,3,2,1]), [1,2,3,4,5,6])
        self.assertEqual(sort.quick_sort([9,8,7,6,5,4,3,2,1]), [1,2,3,4,5,6,7,8,9])

if __name__ == '__main__':
    unittest.main()