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


def two_sum(nums, target) -> list[int]:

    seen = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # list is 0 indexed
    target = 5
    print(two_sum(nums, target))  # [1, 2]
