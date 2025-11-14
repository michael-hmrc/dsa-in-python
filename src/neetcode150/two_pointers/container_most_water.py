# LeetCode 11 — Container With Most Water (Problem Statement)

# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the i-th line are at:

# (i, 0)
# (i, height[i])

# Find two lines that together with the x-axis form a container that holds the maximum amount of water.
# Return the maximum amount of water a container can store.

# Optimal Approach — Two Pointers (O(n))

# heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]

# Each index represents an x-coordinate, and each value represents the height of a vertical line.
# Two lines + the x-axis form a container.
# We want the maximum possible area.

# example:
#     |     
#     |     |
# |   |     |       |
# | | |     |   |   | 
# -----------------------
# 0 1 2 3 4 5 6  7  8 (index)


# │             │    ← sticks
# │             │
# │             │
# │             │
# │_____________│  ← water
# 1            8  ← indices


def container_most_water(height):
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        width = right - left
        h = min(height[left], height[right])
        max_area = max(max_area, width * h)

        if height[left] < height[right]:     #we only move the shorter line since moving the taller line does nothing useful to affect the height of the container
            left += 1           # left line was shorter
        else:
            right -= 1          # move if right line was shorter
 
    return max_area
    
    
if __name__ == "__main__":    
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(container_most_water(height))