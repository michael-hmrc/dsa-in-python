
def is_anagram(s, t):
    return sorted(s) == sorted(t)


# Hash map version:

from collections import Counter

def is_anagram(s, t):
    return Counter(s) == Counter(t)