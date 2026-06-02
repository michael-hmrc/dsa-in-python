height = [0,1,0,2,1,0,1,3,2,1,2,1]


# ============================================================
# Trapping Rain Water
# ============================================================
#
# The question:
#
# Given a list of wall heights, calculate how much water can be trapped.
#
# Example:
#
# height = [2, 0, 2]
#
# This traps 2 units of water:
#
#   #
#   # ~ #
#   # ~ #
# [2,0,2]
#
# The middle position has height 0.
# The wall on the left is height 2.
# The wall on the right is height 2.
#
# So water at the middle = min(2, 2) - 0 = 2
#
#
# The key formula is:
#
# water_at_i = min(left_max, right_max) - height[i]
#
# left_max  = tallest wall from the left up to index i
# right_max = tallest wall from the right up to index i
#
# We use min(left_max, right_max) because water can only rise as high
# as the shorter boundary.
#
# ============================================================


# ============================================================
# Version 1: Brute Force - O(n²)
# ============================================================
#
# For every index:
#
# 1. Look left and find the tallest wall.
# 2. Look right and find the tallest wall.
# 3. The water trapped at this index is:
#
#       min(left_max, right_max) - height[i]
#
# This works, but it is slow because max(height[:i + 1])
# and max(height[i:]) scan parts of the list every time.
#
# Time:  O(n²)
# Space: O(n) because slicing creates new lists
#

def trapping_rainwater_v1(height: list[int]) -> int:
    total_water = 0

    # Check every position in the array
    for i in range(len(height)):

        # Tallest wall from the start up to index i
        left_max = max(height[:i + 1])

        # Tallest wall from index i to the end
        right_max = max(height[i:])

        # Water is limited by the shorter of the two tallest walls
        water_at_i = min(left_max, right_max) - height[i]

        # Add water trapped at this index to the answer
        total_water += water_at_i

    return total_water


# ============================================================
# Version 2: Two Pointer - O(n)
# ============================================================
#
# This is the interview-friendly solution.
#
# Instead of checking left_max and right_max from scratch every time,
# we keep track of them as we move inward.
#
# We use:
#
# left      -> starts at the beginning
# right     -> starts at the end
# left_max  -> highest wall seen so far from the left
# right_max -> highest wall seen so far from the right
#
#
# Core idea:
#
# Move the pointer with the smaller height.
#
# Why?
#
# Because water is controlled by the smaller side.
#
# If height[left] < height[right], then the right side is tall enough
# to trap water on the left side.
#
# So we can safely process the left pointer.
#
# If height[right] <= height[left], then the left side is tall enough
# to trap water on the right side.
#
# So we can safely process the right pointer.
#
# Time:  O(n)
# Space: O(1)

# def trapping_rainwater_v2(height: list[int]) -> int:
    
#     left = 0
#     right = len(height) - 1
#     left_max = 0
#     right_max = 0
#     total_water = 0

#     # Keep moving inward until the two pointers meet
#     while left < right:
#         if height[left] < height[right]:
#             if height[left] >= left_max:
#                 left_max = height[left]
#             else:
#                 total_water += left_max - height[left]
#             left += 1
#         else:
#             if height[right] >= right_max:
#                 right_max = height[right]
#             else:
#                 total_water += right_max - height[right]
#             right -= 1

#     return total_water

def trapping_rainwater_v2(height: list[int]) -> int:
    # Start one pointer at the beginning
    left = 0

    # Start one pointer at the end
    right = len(height) - 1

    # Tallest wall seen so far from the left
    left_max = 0

    # Tallest wall seen so far from the right
    right_max = 0

    # Final result
    total_water = 0

    # Keep going until the two pointers meet
    while left < right:

        # If the left wall is smaller,
        # then the left side controls the water level.
        if height[left] < height[right]:

            # If this wall is taller than left_max,
            # it becomes the new left boundary.
            if height[left] >= left_max:
                left_max = height[left]

            # Otherwise, this wall is lower than left_max,
            # so water can sit above it.
            else:
                total_water += left_max - height[left]

            # Move left pointer inward
            left += 1

        # Otherwise, the right wall is smaller or equal,
        # so the right side controls the water level.
        else:

            # If this wall is taller than right_max,
            # it becomes the new right boundary.
            if height[right] >= right_max:
                right_max = height[right]

            # Otherwise, this wall is lower than right_max,
            # so water can sit above it.
            else:
                total_water += right_max - height[right]

            # Move right pointer inward
            right -= 1

    return total_water



print(trapping_rainwater_v2([0,1,0,2,1,0,1,3,2,1,2,1]))    # 6
print(trapping_rainwater_v2([4,2,0,3,2,5]))                # 9
print(trapping_rainwater_v2([2,0,2]))                      # 2
print(trapping_rainwater_v2([]))                           # 0
print(trapping_rainwater_v2([1,2,3]))                      # 0