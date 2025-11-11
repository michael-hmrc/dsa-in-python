class ContainsDuplicate:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

            
if __name__ == "__main__":
    solution = ContainsDuplicate()
    nums = [1, 2, 3, 1]
    # print(solution.containsDuplicate(nums))  # should print True
    print(solution.containsDuplicate2(nums))  # should print True
