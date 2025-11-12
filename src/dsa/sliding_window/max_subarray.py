# Time: O(n) — we slide the window once across the array
# Space: O(1) — only a few variables

# def max_sum_subarray(nums: list[int], k: int) -> int:
#     # Step 1: Calculate sum of the first window (first k elements)
#     window_sum = sum(nums[:k])
#     max_sum = window_sum
    
#     # Step 2: Slide the window across the array
#     for i in range(k, len(nums)):
#         window_sum += nums[i] - nums[i-k]  # Subtract the element that's no longer in the window nums[i-k]  # Add the new element nums[i]
#         max_sum = max(max_sum, window_sum)
    
#     return max_sum

def max_sum_subarray(nums: list[int], k :int) -> int:
    window_sum = sum(nums[:k])
    max_sum = window_sum
    
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i-k] 
        max_sum = max(max_sum, window_sum)
    return max_sum

if __name__ == "__main__":
    nums = [2, 1, 5, 1, 3, 2]
    k = 3
    print(max_sum_subarray(nums, k))  # Output: 9 ([5,1,3])



