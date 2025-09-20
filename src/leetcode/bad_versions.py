# Fake API for illustration
def isBadVersion(version: int) -> bool:
    return version >= 4  # Example: version 4 and onward are bad


def firstBadVersion(n: int) -> int:
    low = 1
    high = n

    while low < high:
        mid = (low + high) // 2
        if isBadVersion(mid):
            high = mid
        else:
            low = mid + 1
    return low


def firstBadVersionArray(versions: list[bool]) -> int:
    low, high = 0, len(versions) - 1

    while low < high:
        mid = (low + high) // 2
        if versions[mid]:  # bad
            high = mid
        else:  # good
            low = mid + 1
    return low


if __name__ == "__main__":

    n = 5

    print("First bad version is:", firstBadVersion(n))

    versions = [False, False, False, True, True, True]
    print(firstBadVersionArray(versions))  # 3 (0-based index)
