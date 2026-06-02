def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]  # we return indexes of the numbers needed
        seen[num] = i  # we store the zipped index in the map/dict

    return []


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # list is 0 indexed
    target = 8
    print(two_sum(nums, target))  # [2, 4]


