#### Two-pointer technique

def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) -1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True   


#### Leetcode 125

def valid_palindrome(s: str) -> bool:
    
    left = 0
    right = len(s) - 1
    
    while left < right:
        
        # 1. Skip non-alphanumeric characters
        while (left < right) and not s[left].isalnum():
            left += 1
        
        while left < right and not s[right].isalnum():
            right -= 1
        
        # 2. Compare lowercase versions
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

     

if __name__ == "__main__":
    
    palindrome_string = "racecar"
    palindrome_string2 = "aca"
    not_palindrome_string = "michael"
    
    print(is_palindrome(palindrome_string))
    print(is_palindrome(palindrome_string2))
    print(is_palindrome(not_palindrome_string))
    
    print(valid_palindrome(palindrome_string))
    print(valid_palindrome(palindrome_string2))
    print(valid_palindrome(not_palindrome_string))