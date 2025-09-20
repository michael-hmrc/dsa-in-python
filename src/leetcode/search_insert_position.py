# Problem

# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

#  we must return the search position here


def search_insert_position(nums: list[int], target: int) -> int:

    if len(nums) == 0:
        return -1

    low: int = 0
    high: int = len(nums) - 1

    while low <= high:
        mid: int = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return low


if __name__ == "__main__":

    nums = [1, 3, 5, 6]

    print(search_insert_position(nums, 5))  # target exists → 2
    print(search_insert_position(nums, 2))  # should go between 1 and 3 → 1
    print(search_insert_position(nums, 7))  # greater than all → 4
    print(search_insert_position(nums, 0))  # smaller than all → 0
