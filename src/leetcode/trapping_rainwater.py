height = [0,1,0,2,1,0,1,3,2,1,2,1]

# Brute force - O(n²)

def trap(height: list[int]) -> int:
    total_water = 0

    for i in range(len(height)):
        left_max = max(height[:i + 1])
        right_max = max(height[i:])

        water_at_i = min(left_max, right_max) - height[i]

        total_water += water_at_i

    return total_water



def trap(height: list[int]) -> int:
    left = 0
    right = len(height) - 1

    left_max = 0
    right_max = 0

    total_water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                total_water += left_max - height[left]

            left += 1

        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                total_water += right_max - height[right]

            right -= 1

    return total_water


print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # 6
print(trap([4,2,0,3,2,5]))                # 9
print(trap([2,0,2]))                      # 2
print(trap([]))                           # 0
print(trap([1,2,3]))                      # 0