from typing import List, Optional

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def linear_search(arr: List[any], desired_value: any) -> Optional[int]:
    index = -1

    for i in range(len(arr)):
        if arr[i] == desired_value:
            index = i
            break

    if index != -1:
        print(f"Element {desired_value} found at index {index}.")
        return Optional[index]
    else:
        print(f"Element {desired_value} not found in the array.")
        return None


if __name__ == "__main__":
    print(linear_search(arr, 5))
