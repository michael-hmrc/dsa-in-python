# We will use lists to mimic arrays for now
from typing import List

if __name__ == "__main__":

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"initial array: {arr}")

    first_index = arr[0]
    print(f"first_index: {first_index}")

    second_index = arr[1]
    print(f"second_index: {second_index}")

    third_index = arr[2]
    print(f"third_index: {third_index}")

    arr[2] = 999  # mutating and setting third_index value to  999
    print(f"updated array: {arr}")

    arr.append(6)

    print(f"append to array: {arr}")

    arr.pop()  # removes the last element
    print(f"pop array: {arr}")

    print(f"before removal: {arr}")
    arr.remove(999)
    print(f"remove 999: {arr}")

    # traversal of arrays

    def print_out_each_elem(array: List[any]) -> None:
        for elem in array:
            print(elem)

    print_out_each_elem(arr)
