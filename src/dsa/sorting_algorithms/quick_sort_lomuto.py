from typing import List
    
#   Lomuto partition scheme:
#   Moves elements smaller than pivot to the left.
#   Returns the index where the pivot finally lies.
    
import time    
    
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
    
    arr = [66, 22, 11, 33, 99, 77, 55, 88, 0]
    
    start = time.time()                                     # record the start time
    result = quick_sort_in_place(arr, 0, len(arr) - 1)      # run your function
    end = time.time()                                       # record the end time

    print("Sorted: ", result)
    print(f"Time Taken: {end - start:.6f} seconds")