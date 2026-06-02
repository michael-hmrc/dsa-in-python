# LeetCode 217 — Contains Duplicate
# Question:
# Given an integer array nums, return True if any value appears at least twice
# in the array. Return False if every element is distinct.

def contains_duplicate(nums: list[int]) -> bool:
    seen = set()            # we use the set to store numbers we've seen previously
    
    for n in nums:          # loop through each number 
        if n in seen:       # conditional to check if we've seen this number before
            return True     # duplicate found
        seen.add(n)         # store the number in the set
    return False            # no duplicates found
        

if __name__ == "__main__":

    nums = [1, 2, 3, 1]
    print(contains_duplicate(nums))  # should print True
