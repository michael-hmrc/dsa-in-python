
def move_all_zeros_end(nums:list[int]) -> list[int]:
    
    slow = 0  # slow acts as the writer pointer
    
    for fast in range(len(nums)):      # fast pointer is the reader
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]        # Swap non-zero to front
            slow += 1
    return nums
        

def move_all_zeros_end(nums: list[int]) -> list[int]:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            temp = nums[slow]
            nums[slow] = nums[fast]
            nums[fast] = temp
            slow += 1
    return nums
    
if (__name__ == "__main__"):
    
    arr = [0,1,0,3,12]
    move_all_zeros_end(arr)
    print(arr)  # [1, 3, 12, 0, 0]
