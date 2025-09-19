from typing import List

def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # choosing middle point as pivot
    left = [x for x in arr if x < pivot]  # elements less than the pivot
    middle = [x for x in arr if x == pivot]  # elements less than the pivot
    right = [x for x in arr if x > pivot]  # elements less than the pivot

    return quick_sort(left) + middle + quick_sort(right)


def partition(arr: list[int], low: int, high:int):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_in_place(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort_in_place(arr, low, pivot_index - 1)
        quick_sort_in_place(arr, pivot_index + 1, high)
