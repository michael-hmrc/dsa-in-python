
# LeetCode 27

def remove_elements(arr: list[int], val:int) -> list[int]:
    
    slow = 0
    for fast in range(len(arr)):
        if arr[fast] != val:
            arr[slow] = arr[fast]
            slow += 1
    return slow    # we return the number of elements in the list
    
    
if (__name__ == "__main__"):
    nums = [1,1,2,2,3]
    val = 1
    length = remove_elements(nums, val)
    print(length, nums[:length])                    # 3 elements with list == [2, 2, 3]
