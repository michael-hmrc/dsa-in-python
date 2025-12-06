from typing import List
import time

# def insertion_sort(arr: List[int]) -> List[int]:
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1  # starts on 0

#         # take the current value and compare to the value on left hand side, if lhs < rhs then proceed to the swap
#         while j >= 0 and key < arr[j]:
#             # first run arr[j + 1] = 11
#             arr[j + 1] = arr[j]  # this performs the swap, arr[j] = 12, now set arr[j + 1] = 12
#             j -= 1               # on first pass this is set to -1
#         print(j)
#         arr[j + 1] = key
#         # we then leave the while loop and arr[0] = arr[-1 +1] will then set 11 in the 0 index of the array
#         # we then continue the for loop with i =2
#     return arr


def insertion_sort(arr: List[int]) -> List[int]:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1  # starts on 0
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    
    arr = [66, 22, 11, 33, 99, 77, 55, 88, 0]
    
    start = time.time()            # record the start time
    result = insertion_sort(arr)   # run your function
    end = time.time()              # record the end time

    print("Sorted: ", result)
    print(f"Time Taken: {end - start:.6f} seconds")