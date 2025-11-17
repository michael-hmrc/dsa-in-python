# -------------------------
# Python Set Rules / Notes
# -------------------------
# 1. Sets are UNORDERED  → no indexing (you can't do s[0])
# 2. Sets contain UNIQUE values (duplicates removed automatically)
# 3. Membership checks are O(1)  → fast lookup (x in s)
# 4. Cannot store mutable items (e.g. no lists) but can store tuples
# 5. Use sets for:
#       - avoiding duplicates
#       - tracking visited nodes
#       - fast membership checks
#       - intersections, unions, differences
# 6. Common operations:
#       s.add(x)
#       s.remove(x)     # errors if x missing
#       s.discard(x)    # safe remove
#       s.clear()
# 7. Mathematical operations:
#       s1 | s2   → union
#       s1 & s2   → intersection
#       s1 - s2   → difference
#       s1 ^ s2   → symmetric difference
# -------------------------


def print_target(a: set[int], target: int) -> None:
    if target in a:
        print(f"{target} exists in the set!")
    else:
        print("Not found")


def setConditional(set_num: set[int]) -> None:
    for x in set_num:
        if x % 2 == 0:  # conditional check
            print(x)


def print_common(a: set[int], b: set[int]) -> None:
    for x in a:
        if x in b:  # conditional set check
            print(x)
            
            

if __name__ == "__main__":
    my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    print("transformed my set into a list: " + str(list(my_set)))
    print_target(my_set, 3)


