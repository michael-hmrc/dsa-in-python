# We can check things in various data structures to hold the elements to check

def checkVowelInTuple(x: str) -> None:
    if x in ("a", "e", "i"):
        print(f"{x} is a vowel (checked with tuple)")
    else:
        print(f"{x} is not a vowel")


def checkVowelInList(x: str) -> None:
    if x in ["a", "e", "i"]:
        print(f"{x} is a vowel (checked with list)")
    else:
        print(f"{x} is not a vowel")


def checkVowelInSet(x: str) -> None:
    vowels = {"a", "e", "i", "o", "u"}
    if x in vowels:
        print(f"{x} is a vowel (checked with set)")
    else:
        print(f"{x} is not a vowel")
