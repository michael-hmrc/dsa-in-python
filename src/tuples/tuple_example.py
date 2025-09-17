from typing import Tuple

# Homogeneous tuple of ints
tuple1: Tuple[int, int, int] = (1, 2, 3)

# Mixed types: int, str, float
t2: Tuple[int, str, float] = (1, "hello", 3.14)

# Same as tuple1
t3: Tuple[int, int, int] = (1, 2, 3)

# Single-element tuple of int
t4: Tuple[int] = (5,)

# This is just an int
not_tuple: int = (5)

# 4 integers
t: Tuple[int, int, int, int] = (10, 20, 30, 40)

print(t[0])   # 10
print(t[-1])  # 40
print(t[1:3]) # (20, 30) → slicing returns Tuple[int, int]

# Tuple unpacking
point: Tuple[int, int] = (3, 4)
x, y = point
print(x)  # 3
print(y)  # 4
