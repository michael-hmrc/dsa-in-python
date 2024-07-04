import pytest

from sorting_algorithms.quick_sort import quick_sort


# Test case 1: Basic test with positive integers
def test_quick_sort_basic():
    assert quick_sort([3, 6, 8, 10, 1, 2, 1]) == [1, 1, 2, 3, 6, 8, 10]

# Test case 2: Test with negative integers
def test_quick_sort_negative():
    assert quick_sort([-5, -10, 0, 5, 10]) == [-10, -5, 0, 5, 10]

# Test case 3: Test with repeated elements
def test_quick_sort_repeated():
    assert quick_sort([5, 3, 8, 3, 2, 8, 1]) == [1, 2, 3, 3, 5, 8, 8]

# Test case 4: Test with an empty list
def test_quick_sort_empty():
    assert quick_sort([]) == []

# Test case 5: Test with a single element
def test_quick_sort_single():
    assert quick_sort([1]) == [1]

# Test case 6: Test with already sorted list
def test_quick_sort_sorted():
    assert quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

# Test case 7: Test with a reverse sorted list
def test_quick_sort_reverse_sorted():
    assert quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

# Test case 8: Test with large numbers
def test_quick_sort_large_numbers():
    assert quick_sort([1000000, 999999, 0, -999999, -1000000]) == [-1000000, -999999, 0, 999999, 1000000]

# Run pytest
if __name__ == "__main__":
    pytest.main()