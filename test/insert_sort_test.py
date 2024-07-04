import unittest

from src.insert_sort import insertion_sort


class TestInsertionSpec(unittest.TestCase):

    def test_sorted_array(self) -> None:
        # print(insertion_sort([1, 2, 3, 4, 5]))
        self.assertEqual(insertion_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self) -> None:
        self.assertEqual(insertion_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_array(self) -> None:
        self.assertEqual(insertion_sort([12, 11, 13, 5, 6]), [5, 6, 11, 12, 13])

    def test_array_with_duplicates(self) -> None:
        self.assertEqual(insertion_sort([4, 5, 4, 3, 4]), [3, 4, 4, 4, 5])

    def test_empty_array(self) -> None:
        self.assertEqual(insertion_sort([]), [])

    def test_single_element_array(self) -> None:
        self.assertEqual(insertion_sort([1]), [1])


if __name__ == '__main__':
    unittest.main()
