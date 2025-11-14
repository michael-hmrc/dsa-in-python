
def freq(s):
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    return count


