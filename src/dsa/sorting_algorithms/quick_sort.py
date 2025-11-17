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

def quick_sort(arr: List[int]) -> List[int]:

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# Duplicate version (same Big-O applies)
def quick_sort(arr: list[int]) -> list[int]:

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    arr = [3, 6, 2, 8, 5, 1]
    print("Functional QuickSort:", quick_sort(arr))
