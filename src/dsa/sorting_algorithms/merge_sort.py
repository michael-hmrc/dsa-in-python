#  Splitting takes O(log n) levels.
#  Merging takes O(n) at each level.
#  Overall: O(n log n) time.
#  Space: O(n) (for extra arrays).


def merge_sort(arr):
    # Base case: 1 element is already sorted
    if len(arr) <= 1:
        return arr

    # Split into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left: list[int], right: list[int]) -> list[int]:

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Original:", arr)
    print("Sorted:", merge_sort(arr))
