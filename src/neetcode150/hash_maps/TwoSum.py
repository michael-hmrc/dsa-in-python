class TwoSum:    
    
    def twoSum(self, nums: list[int], target:int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums): 
            diff = target - num
            if diff in seen:    
                return [seen[diff], i]
            seen[num] = i
        return []     


if __name__ == "__main__":
    solution = TwoSum()
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   # list is 0 indexed
    target = 5
    print(solution.twoSum(nums, target)) 