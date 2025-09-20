from typing import List


def insertion_sort(arr: List[int]) -> List[int]:
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1  # starts on 0

        # take the current value and compare to the value on left hand side, if lhs < rhs then proceed to the swap
        while j >= 0 and key < arr[j]:
            # first run arr[j + 1] = 11
            arr[j + 1] = arr[
                j
            ]  # this performs the swap, arr[j] = 12, now set arr[j + 1] = 12
            j -= 1  # on first pass this is set to -1
        print(j)
        arr[j + 1] = key
        # we then leave the while loop and arr[0] = arr[-1 +1] will then set 11 in the 0 index of the array
        # we then continue the for loop with i =2
    return arr
