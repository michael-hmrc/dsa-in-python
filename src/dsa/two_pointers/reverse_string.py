

# pythonic
def reverse_string(s:list[str]) -> str:
    left = 0
    right = len(s) -1    
    
    while left < right:
        s[left], s[right] = s[right], s[left]. 
        left +=1
        right -=1
    return s



def reverse_string(s:list[str]) -> str:
    left = 0
    right = len(s) -1    
    
    while left < right:
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
        left +=1
        right -=1
    return s
        
if __name__ == "__main__":
    s = ["m", "i", "c", "h", "a", "e", "l"]
    print(reverse_string(s))   