
def two_sum(nums, target):

    # we use a dictionary here to store the complement of each number and its index

    num_map = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []