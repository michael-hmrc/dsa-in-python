from two-pointers import two_sum

if __name__ == "__main__":
    # Example usage:
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))  # Output: [0, 1] (because nums[0] + nums[1] = 2 + 7 = 9)

    # Example usage with a larger list:
    nums_large = [1, 9, 3, 7, 5, 11, 2, 8, 6, 4]
    target_large = 15
    print(f"nums_large: {nums_large}")
    print(f"target_large: {target_large}")
    print(f"Indices of the two numbers that sum up to {target_large}: {two_sum(nums_large, target_large)}")
