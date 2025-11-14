
# Variable sliding window

# Longest Substring Without Repeating Characters (Sliding Window)
# Fast expands window, slow shrinks it.

def length_of_longest_substring(string: str) -> int:
    
    seen = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        # If duplicate, shrink window from left
        while string[right] in seen:
            seen.remove(string[left])
            left += 1
        
        seen.add(string[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len