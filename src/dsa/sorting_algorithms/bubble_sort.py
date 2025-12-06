# Bubble Sort
# ------------
# Big O Time Complexity:
#   Worst Case:   O(n^2)
#   Average Case: O(n^2)
#   Best Case:    O(n)     (because we stop early if no swaps occur)
#
# Space Complexity:
#   O(1) — in-place sorting
#
# How it works:
#   - Repeatedly loop through the list.
#   - Compare adjacent elements.
#   - Swap them if they’re in the wrong order.
#   - After each full pass, the largest remaining element "bubbles" to the end.
#   - Optimization: if an entire pass has no swaps, the list is already sorted.
#
# Example of the process:
#   [5, 3, 8, 4, 2]
#    → bubble pass → largest goes to the end
#   Repeat until sorted.

import time

def bubble_sort(nums):
    n = len(nums)

    for i in range(n):
        swapped = False  # track whether any swap happens in this pass

        # The last i elements are already sorted, so skip them
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True

        # If no swaps occurred, the list is sorted early
        if not swapped:
            break

    return nums


def bubble_sort(arr) -> list[int]:

    length = len(arr)

    for i in range(length):
        swapped = False
        for j in range(0, length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr


if __name__ == "__main__":
    nums = [66, 22, 11, 33, 99, 77, 55, 88, 0]
    
    start = time.time()            # record the start time
    result = bubble_sort(nums)     # run your function
    end = time.time()              # record the end time

    print("Sorted: ", result)
    print(f"Time Taken: {end - start:.6f} seconds")