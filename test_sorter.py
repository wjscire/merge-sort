import unittest
from sorter import merge_sort
class TestSorter(unittest.TestCase):

    def setUp(self):
        self.a = [1, 1, 1]
        self.b = [4, 3, 2, 1]
        self.c = [4]
        self.d = []
        self.e = [1, 0, 1, 0, 1, 0]
        self.f = [2, 4, 6, 8]
        merge_sort(self.a)
        merge_sort(self.b)
        merge_sort(self.c)
        merge_sort(self.d)
        merge_sort(self.e)
        merge_sort(self.f)

    def test_merge_sort(self):
        self.assertEqual(self.a, [1, 1, 1])
        self.assertEqual(self.b, [1, 2, 3, 4])
        self.assertEqual(self.c, [4])
        self.assertEqual(self.d, [])
        self.assertEqual(self.e, [0, 0, 0, 1, 1, 1])
        self.assertEqual(self.f, [2, 4, 6, 8])

if __name__ == "__main__":
    unittest.main()
