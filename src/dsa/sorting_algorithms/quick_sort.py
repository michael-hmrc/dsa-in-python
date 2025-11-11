from typing import List

# ------------------------------
# 🧩 1. Simple Recursive QuickSort (returns a new list)
# ------------------------------
def quick_sort(arr: List[int]) -> List[int]:
    """
    Simple functional (non-in-place) implementation of QuickSort.
    Returns a new sorted list.
    """
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr

    # Choose a pivot (here we use the middle element for balance)
    pivot = arr[len(arr) // 2]

    # Partition into three lists:
    # - left: elements smaller than pivot
    # - middle: elements equal to pivot
    # - right: elements greater than pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Recursively sort left and right partitions
    return quick_sort(left) + middle + quick_sort(right)


# ------------------------------
# 🧩 2. In-Place QuickSort (mutates the array)
# ------------------------------
def partition(arr: List[int], low: int, high: int) -> int:
    """
    Lomuto partition scheme:
    Moves elements smaller than pivot to the left.
    Returns the index where the pivot finally lies.
    """
    pivot = arr[high]  # choose the last element as pivot
    i = low - 1        # place for swapping smaller elements

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swap

    # place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_in_place(arr: List[int], low: int, high: int) -> None:
    """
    In-place recursive QuickSort using partition().
    """
    if low < high:
        # Partition the array and get pivot index
        pivot_index = partition(arr, low, high)

        # Recursively sort elements before and after pivot
        quick_sort_in_place(arr, low, pivot_index - 1)
        quick_sort_in_place(arr, pivot_index + 1, high)


# ------------------------------
# 🧪 Example Usage
# ------------------------------
if __name__ == "__main__":
    arr1 = [3, 6, 2, 8, 5, 1]
    print("Functional QuickSort:", quick_sort(arr1))

    arr2 = [3, 6, 2, 8, 5, 1]
    quick_sort_in_place(arr2, 0, len(arr2) - 1)
    print("In-place QuickSort:  ", arr2)
