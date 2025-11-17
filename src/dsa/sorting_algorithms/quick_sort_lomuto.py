from typing import List
    
#   Lomuto partition scheme:
#   Moves elements smaller than pivot to the left.
#   Returns the index where the pivot finally lies.
    
def partition(arr: List[int], low: int, high: int) -> int:

    pivot = arr[high]  # choose the last element as pivot
    i = low - 1        # place for swapping smaller elements

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swap


    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_in_place(arr: List[int], low: int, high: int) -> None:
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort_in_place(arr, low, pivot_index - 1)
        quick_sort_in_place(arr, pivot_index + 1, high)

if __name__ == "__main__":
    arr = [3, 6, 2, 8, 5, 1]
    quick_sort_in_place(arr, 0, len(arr) - 1)
    print("In-place QuickSort:  ", arr)
