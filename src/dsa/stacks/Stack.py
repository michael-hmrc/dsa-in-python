"""
Stack Notes
===========

A stack is a data structure that follows LIFO:

    LIFO = Last In, First Out

This means the last item added is the first item removed.

Example:

    stack.push(10)
    stack.push(20)
    stack.push(30)

    stack.pop()  -> returns 30

Python stack idea:
------------------

In Python, we can use a list to build a stack.

The end of the list is treated as the "top" of the stack.

Example:

    [10, 20, 30]
             ↑
            top

Main stack operations:
----------------------

push(value)
    Add a value to the top of the stack.

pop()
    Remove and return the value from the top of the stack.

peek()
    Look at the value on top of the stack without removing it.

is_empty()
    Check whether the stack has no items.

size()
    Return how many items are currently in the stack.

Why stacks are useful:
----------------------

Stacks are useful when the most recent thing matters first.

Common examples:

    - Undo feature
    - Browser back button
    - Function call stack
    - Valid parentheses problems
    - Depth-first search
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)