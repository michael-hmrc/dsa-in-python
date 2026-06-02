# Leetcode 3 - Longest Substring Without Repeating Characters

# Problem Summary (simplified)

# Given a string s, find the length of the longest substring that contains no repeating characters.
# A substring means continuous characters.
# You cannot reorder characters — only read left→right.
# You must return the length, not the substring

# Input: "abcabcbb"
# Output: 3
# Explanation: "abc" is the longest substring


def length_of_longest_substring(s: str) -> int:

    left = 0
    seen = set()
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len


if __name__ == "__main__":
    string = "abcabcbb"
    print(length_of_longest_substring(string))
