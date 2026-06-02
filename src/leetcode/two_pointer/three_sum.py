# Given an integer array nums, return all unique triplets [a, b, c] such that:
# a + b + c == 0

# Optimal Approach (O(n²)) — Sort + Two Pointers

# Key idea:

# 1. Sort the array
# 2. Fix one number i
# 3. Use two pointers (left and right) to solve a 2Sum on the remaining array
# 4. Skip duplicates so results stay unique

def three_sum(nums):
    
    nums.sort()
    result = []

    for i in range(len(nums)):
        # skip same number to avoid duplicates in result
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left = i + 1
        right = len(nums) - 1

        while left < right:
            s = nums[i] + nums[left] + nums[right]

            if s < 0:
                left += 1
            elif s > 0:
                right -= 1
            else:  # found a triplet
                result.append([nums[i], nums[left], nums[right]])

                # skip duplicate left
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                # skip duplicate right
                right -= 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
    
    return result


if __name__ == "__main__":
    
    nums = [-1, 0, 1, 2, -1, -4]
    print(three_sum(nums))
