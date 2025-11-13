# Remove Duplicates from a Sorted List (Return New Length)
# This uses two pointers moving forward.
# slow and fast pointer - slow == write, fast == read
# one read, one write pointer

def remove_duplicates(nums):
    if not nums:
        return 0
    
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    
    return slow + 1


if (__name__ == "__main__"):
    nums = [1,1,2,2,3]
    length = remove_duplicates(nums)
    print(length, nums[:length])  # 3 [1, 2, 3]
