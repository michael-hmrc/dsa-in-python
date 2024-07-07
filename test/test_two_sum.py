import pytest

from two_pointers.two_sum import two_sum  # Assuming two_sum function is implemented in a separate module


# Test case 1: Simple case with positive numbers
def test_two_sum_positive():
    nums = [2, 7, 11, 15]
    target = 9
    assert two_sum(nums, target) == [0, 1]


# Test case 2: Larger list with unique solution
def test_two_sum_larger_unique():
    nums = [3, 10, 5, 8, 6, 12, 1, 4, 9, 7]
    target = 15
    assert two_sum(nums, target) == [1, 2]


# Test case 3: Larger list with no solution
def test_two_sum_larger_no_solution():
    nums = [6, 8, 3, 12, 5, 17, 9, 2, 11, 4]
    target = 30
    assert two_sum(nums, target) == []


# Test case 4: Negative numbers
def test_two_sum_negative():
    nums = [-3, 5, -2, 8, -6, 11, 4, -1, 7, 9]
    target = 3
    assert two_sum(nums, target) == [1, 2]


# Test case 5: Edge case - Empty list
def test_two_sum_empty_list():
    nums = []
    target = 5
    assert two_sum(nums, target) == []


# Run pytest
if __name__ == "__main__":
    pytest.main()
