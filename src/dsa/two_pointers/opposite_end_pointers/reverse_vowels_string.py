
def reverse_vowels_in_string(s: str) -> str:
    vowels = set("aeiouAEIOU")
    stringArray = list(s)
    left, right = 0, len(stringArray) - 1

    while left < right:
        if stringArray[left] not in vowels:
            left += 1
        elif stringArray[right] not in vowels:
            right -= 1
        else:
            stringArray[left], stringArray[right] = stringArray[right], stringArray[left]
            left += 1
            right -= 1

    return "".join(stringArray)