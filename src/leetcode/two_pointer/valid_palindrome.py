
def valid_palindrome(s:str) -> bool:
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left +=1 
        right -=1 
    return True        


if __name__ == "__main__":
    
    palindrome_string = "racecar"
    palindrome_string2 = "aca"
    not_palindrome_string = "michael"
    
    print(valid_palindrome(palindrome_string))          # True
    print(valid_palindrome(palindrome_string2))         # True
    print(valid_palindrome(not_palindrome_string))      # False