# LeetCode 167 - Two Sum II (Input Array is Sorted)
# -------------------------------------------------
# Notes:
# - This is a classic Two Pointers problem.
# - Use when the array is sorted.
# - We move pointers inward based on whether the sum is too big or too small.
# - Time Complexity: O(n)
# - Space Complexity: O(1)


#### returns a bool to denote the return of successful summation
# def has_pair_with_sum(nums: list[int], target: int) -> bool:

#     left = 0
#     right = len(nums) - 1

#     while left < right:
#         s = nums[left] + nums[right]

#         if s == target:
#             return True
#         elif s < target:
#             left += 1       # need a larger number → move left pointer right
#         else:
#             right -= 1      # need a smaller number → move right pointer left

#     return False


#### returns the numbers to make target
def has_pair_with_sum(num, target) -> list[int]:
    
    left, right = 0, len(num) - 1 
    
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return [nums[left], nums[right]]
        elif s < target:
            left +=1
        else:
            right -= 1
    return []


def basic_valid_palindrome(s:str) -> bool:
    
    left = 0 
    right = len(s) -1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


#### Leetcode 125

def valid_palindrome(s: str) -> bool:
    
    left = 0
    right = len(s) - 1
    
    while left < right:
        
        # 1. Skip non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
        
        while left < right and not s[right].isalnum():
            right -= 1
        
        # 2. Compare lowercase versions
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

if __name__ == "__main__":

    # nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # sorted array
    # target = 4

    # print(has_pair_with_sum(nums, target))
    
    s = "race a car"
    print(valid_palindrome(s))
