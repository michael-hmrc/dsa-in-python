# variable size sliding window problem

# We need a contiguous subarray.
# A brute force approach would check all subarrays → O(n²). Too slow.

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length of 2.

def min_subarray_len(target: int, nums: list[int]) -> int:
    left = 0
    window_sum = 0
    min_len = float("inf")
    
    for right in range(len(nums)):
        window_sum += nums[right]
        
        # Shrink while window is valid
        while window_sum >= target:
            min_len = min(min_len, right - left + 1)  # ✅ key update
            window_sum -= nums[left]   # remove leftmost element
            left += 1                  # shrink window
    
    return 0 if min_len == float("inf") else min_len


def min_subarray_len_bruteforce(target: int, nums: list[int]) -> int:
    n = len(nums)
    min_len = float("inf")
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum >= target:
                min_len = min(min_len, j - i + 1)
                break  # no need to expand further from this i
    
    return 0 if min_len == float("inf") else min_len


if __name__ == "__main__":
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    print("Array:", nums, "Target:", target)
    result = min_subarray_len(target, nums)
    print("Result:", result)