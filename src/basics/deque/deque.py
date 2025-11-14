# deque stands for double-ended queue.

# You import it like this:
# from collections import deque

# It is basically a queue that allows:

# fast append to the right
# fast append to the left
# fast pop from the right
# fast pop from the left

# All in O(1) time.

# This makes it perfect for BFS.


from collections import deque

queue = deque()
# queue.append(start)   # enqueue

queue.append(1)  # queue = [0, 1]
queue.append(2)  # queue = [0, 1, 2]

queue.popleft()  # returns 0 → queue = [1, 2]
queue.popleft()  # returns 1 → queue = [2]

# Deque can also behave like a stack:

stack = deque()
stack.append(10)
stack.append(20)
stack.append(30)

print(stack.pop())  # 30
print(stack.pop())  # 20


if __name__ == "__main__":
    print(1)
