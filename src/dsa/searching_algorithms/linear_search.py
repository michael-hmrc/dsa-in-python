from typing import List, Optional


def linear_search(nums: list[int], target: int) -> int:

    if len(nums) == 0:
        return -1

    for i in range(len(arr)):
        if arr[i] == target:
            return i


if __name__ == "__main__":

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(linear_search(arr, 5))  # should be index == 4
