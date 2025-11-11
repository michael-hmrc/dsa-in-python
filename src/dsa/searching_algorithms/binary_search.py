# #  we are halving here so likely - log n

# # So worst-case time = O(log n)
# # So best-case time = O(1) - immediate found mid as the solve

# # Your iterative version only uses a few extra variables (low, high, mid) → O(1) space.
# # A recursive version would use the call stack, so O(log n) space.



def binary_search(arr:list[int], target: int) -> int:
    
    if len(arr) == 0:
        return -1
    
    low: int = 0
    high: int = len(arr) -1
    
    while low <= high:
        mid: int = (low + high) // 2
        if target == arr[mid]:
            return mid
        if target < arr[mid]:
            high = mid - 1.0
        if target > arr[mid]:
            low = mid + 1.0
            
    

if __name__ == "__main__":

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 5

    print(binary_search(nums, target))  # should return index 4
