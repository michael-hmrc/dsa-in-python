# def two_sum(nums: list[int], target: int) -> list[int]:
#     seen = {}
#     for i, num in enumerate(nums):
#         diff = target - num
#         if diff in seen:
#             return [seen[diff], i]
#         seen[num] = i
#     return []


# def two_sum(nums, target) -> list[int]:

#     seen = {}       # stores the numbers we
#     for i, num in enumerate(nums):                  # enumerate is basically zip with index, hence the i, nums
#         diff = target - num
#         if diff in seen:
#             return [seen[diff], i]
#         seen[num] = i                               # we set seen[num] to be the index
#     return []


def two_sum(nums, target):
    
    seen = {} # this question we use a dictionary or map in other languages
    
    for i, num in enumerate(nums):      
        diff = target - num
        if diff in seen: 
            return [seen[diff], i]    # we return indexes of the numbers needed
        seen[num] = i                 # we store the zipped index in the map/dict
    return []    # return nothing if there are no two numbers which sum up to the target
        
    
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # list is 0 indexed
    target = 8
    print(two_sum(nums, target))  # [2, 4]
