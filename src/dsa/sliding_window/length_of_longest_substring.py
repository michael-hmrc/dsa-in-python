# LeetCode 3 — Longest Substring Without Repeating Characters
# ----------------------------------------------------------
# Problem:
#   Given a string s, return the length of the longest substring
#   that contains no repeating characters.
#
# Key Idea — Variable Sliding Window:
#   • Use two pointers: left (slow) and right (fast).
#   • Right expands the window by adding characters.
#   • If we see a duplicate, move 'left' forward until duplicate is removed.
#   • Use a set to track which characters are in the current window.
#
# Why this works:
#   The window always contains unique characters.
#   Every character is added once and removed once → O(n) time.
# ----------------------------------------------------------

# def length_of_longest_substring_no_repeating_chars(string: str) -> int:
    
#     seen = set()        # Tracks characters currently in the window
#     left = 0            # Start of window
#     max_len = 0         # Longest valid window seen
    
#     for right in range(len(string)):
#         # If the incoming character is a duplicate, shrink from the left
#         while string[right] in seen:
#             seen.remove(string[left])
#             left += 1
        
#         # Include the new character in the window
#         seen.add(string[right])
        
#         # Update longest window size
#         max_len = max(max_len, right - left + 1)
    
#     return max_len


def length_of_longest_substring_no_repeating_chars(string: str) -> int:
    
    seen = set()            # Stores characters currently inside the sliding window
    left = 0                # Left pointer (start of window)
    max_len = 0             # Tracks the longest valid substring with no duplicates
    
    for right in range(len(string)):    
        # If the current character is already in the window,
        # shrink the window from the left until the duplicate is removed
        while string[right] in seen:
            seen.remove(string[left])   # Remove the char at the left pointer from the window
            left += 1                   # Move the left pointer to shrink the window
        
        # Now it's safe to add the current character
        seen.add(string[right])
        
        # Update max window size: (right - left + 1) is the current window length
        max_len = max(max_len, right - left + 1)
        
    return max_len


if __name__ == "__main__":
    string = "abcabcbb"
    print(length_of_longest_substring_no_repeating_chars(string))
