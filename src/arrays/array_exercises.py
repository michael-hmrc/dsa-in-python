

def find_max(nums: list[int]) -> int:
    max_val = float('-inf')  # smallest possible value
    for num in nums:
        if num > max_val:
            max_val = num
    return max_val       


def find_min(nums: list[int]) -> int:
    min_val = float('+inf')  # largest possible value
    for num in nums:
        if num < min_val:
            min_val = num
    return min_val       

def sum(nums: list[int]) -> int:
    acc: int = 0  

    for num in nums:
        acc += num
    return acc     

def get_evens(nums: list[int]) -> list[int]:    

    evens: list[int] = []
    
    for i in nums:
        if i % 2 == 0:
            evens.append(i)
    return evens            
    
def numberOfEvens(nums: list[int]) -> int:    

    counter: int = 0
    
    for i in nums:
        if i % 2 == 0:
            counter += 1
    return counter   

if __name__ == "__main__":

    nums = [1,2,3,4,5,6,7,8,9,10]

    print(find_max(nums))
    print(find_min(nums))
    print(sum(nums))
    print(get_evens(nums))
    print(numberOfEvens(nums))
