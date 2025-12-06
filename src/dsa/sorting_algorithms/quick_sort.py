from typing import List

# -------------------------------------------------------------
# 🧠 QuickSort (Functional, Non-In-Place)
#
# Big-O Complexity:
#   • Average Time:  O(n log n)
#   • Best Time:     O(n log n)
#   • Worst Time:    O(n²)        <-- happens with bad pivot choices
#
#   • Space:         O(n)         <-- because we create new lists
#
# Notes:
#   - This is the simple "functional" style QuickSort.
#   - Not in-place: left/middle/right lists allocate new memory.
#   - Very clean and readable, great for learning.
#   - Pivot choice affects performance (middle is usually good).
# -------------------------------------------------------------

import time

def quick_sort(arr: List[int]) -> List[int]:

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    
    nums = [66, 22, 11, 33, 99, 77, 55, 88, 0]
    
    start = time.time()            # record the start time
    result = quick_sort(nums)     # run your function
    end = time.time()              # record the end time

    print("Sorted: ", result)
    print(f"Time Taken: {end - start:.6f} seconds")