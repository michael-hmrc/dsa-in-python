# LeetCode 424 — Longest Repeating Character Replacement
#
# Problem Summary:
# ----------------
# You are given a string s and an integer k.
#
# You may change (replace) ANY character in the string into ANY other character,
# but you can do this at most k times.
#
# Your goal is to find the **length of the longest substring** that can be turned
# into a string where **all characters are the same**, after performing at most k
# replacements.
#
# In other words:
# - You choose a window (substring).
# - Inside that window, you are allowed to replace up to k characters.
# - After replacements, all characters in the window must match.
# - Your task is to return the maximum possible window length.
#
# Key Insight:
# ------------
# Use a sliding window.
# Track character frequencies inside the window.
# A window is valid if:
#
#     window_size - max_freq_char_count <= k
#
# meaning: “How many characters must we replace to make this window all one char?”
#
# Expand the window while valid; shrink from the left when invalid.
#
# Time Complexity: O(n)
# Space Complexity: O(1) — because at most 26 letters are tracked.
#

def longest_repeating_character_replacement(s: str, k: int) -> int:
    count = {}
    left = 0
    max_freq = 0
    max_len = 0

    for right in range(len(s)):
        char = s[right]
        count[char] = count.get(char, 0) + 1

        # Update the max freq in the current window
        max_freq = max(max_freq, count[char])

        # If the window is invalid, shrink from the left
        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


if __name__ == "__main__":
    string = "AABABBA"
    k = 1
    print(longest_repeating_character_replacement(string, k))
