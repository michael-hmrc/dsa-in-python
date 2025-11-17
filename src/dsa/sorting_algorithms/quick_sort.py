from typing import List
    
#   Simple functional (non-in-place) implementation of QuickSort.
#   Returns a new sorted list.
    
def quick_sort(arr: List[int]) -> List[int]:

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
