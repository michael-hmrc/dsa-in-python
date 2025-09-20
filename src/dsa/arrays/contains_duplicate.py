from typing import List


# Brute force
# Time complexity: O(n²)
# Space complexity: O(1)
def contains_duplicate_bruteforce(nums: List[int]) -> bool:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False


# Sorting
# Time complexity: O(n log n)
# Space complexity: O(1) or O(n)
def contains_duplicate_sort(nums: List[int]) -> bool:
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False


# HashSet (best)
# Time complexity: O(n)
# Space complexity: O(n)
def contains_duplicate_set(nums: List[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# Test in main
if __name__ == "__main__":

    test_cases: list[list[int]] = [
        [1, 2, 3, 1],  # should return True
        [1, 2, 3, 4],  # should return False
        [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],  # should return True
    ]

    test_cases: List[List[int]] = [
        [1, 2, 3, 1],  # should return True
        [1, 2, 3, 4],  # should return False
        [1, 1, 1, 3, 3, 4, 3, 2, 4, 2],  # should return True
    ]

    print("Testing Brute Force:")
    for nums in test_cases:
        print(
            nums, "=>", contains_duplicate_bruteforce(nums[:])
        )  # use nums[:] to not affect sorting

    print("\nTesting Sorting:")
    for nums in test_cases:
        print(nums, "=>", contains_duplicate_sort(nums[:]))

    print("\nTesting HashSet:")
    for nums in test_cases:
        print(nums, "=>", contains_duplicate_set(nums[:]))
