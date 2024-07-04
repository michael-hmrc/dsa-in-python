import unittest

from src.quick_sort import quick_sort, quick_sort_in_place


class TestQuicksort(unittest.TestCase):

    def test_quick_sort_empty(self):
        self.assertEqual(quick_sort([]), [])

    def test_quick_sort_single_element(self):
        self.assertEqual(quick_sort([1]), [1])

    def test_quick_sort_sorted(self):
        self.assertEqual(quick_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_quick_sort_reverse_sorted(self):
        self.assertEqual(quick_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_quick_sort_unsorted(self):
        self.assertEqual(quick_sort([12, 4, 5, 6, 7, 3, 1, 15]), [1, 3, 4, 5, 6, 7, 12, 15])

    def test_quick_sort_duplicates(self):
        self.assertEqual(quick_sort([5, 3, 8, 3, 5, 2, 1]), [1, 2, 3, 3, 5, 5, 8])

    def test_quick_sort_in_place_empty(self):
        arr = []
        quick_sort_in_place(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [])

    def test_quick_sort_in_place_single_element(self):
        arr = [1]
        quick_sort_in_place(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1])

    def test_quick_sort_in_place_sorted(self):
        arr = [1, 2, 3, 4, 5]
        quick_sort_in_place(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_quick_sort_in_place_reverse_sorted(self):
        arr = [5, 4, 3, 2, 1]
        quick_sort_in_place(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_quick_sort_in_place_unsorted(self):
        arr = [12, 4, 5, 6, 7, 3, 1, 15]
        quick_sort_in_place(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1, 3, 4, 5, 6, 7, 12, 15])

    def test_quick_sort_in_place_duplicates(self):
        arr = [5, 3, 8, 3, 5, 2, 1]
        quick_sort_in_place(arr, 0, len(arr) - 1)
        self.assertEqual(arr, [1, 2, 3, 3, 5, 5, 8])
