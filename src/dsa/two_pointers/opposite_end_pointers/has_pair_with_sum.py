
# Problem: Given a sorted list, check if two numbers sum to a target.

def has_pair_with_sum(nums: list[int], target: int) -> bool:
    
    left = 0
    right = len(nums) - 1
    
    while(left < right):
        s = nums[left] + nums[right]
        if s == target:
            return True
        elif s < target:
             left += 1
        else: 
            right -= 1     
    return False


if (__name__ == "__main__"):
    
    nums = [1,2,3,4,5,6,7,8,9,10]
    target = 4
    
    print(has_pair_with_sum(nums, target))