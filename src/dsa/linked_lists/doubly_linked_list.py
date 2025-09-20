# Advanced: Doubly Linked List
#
# For a more advanced linked list, you can implement a doubly linked list where each node has references to both the next
# and the previous nodes. This allows for more efficient backward traversal and deletion operations.

# Example: 1 <-> 2 <-> 3
# pointers in both directions.


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):

        # adds data to the end of the list

        new_node: Node = Node(data)  # initialize a new Node() with the desired data
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def prepend(self, data):

        new_node = Node(data)
        if not self.head:  # If the list is empty
            self.head = new_node
            return

        self.head.prev = new_node  # Link the current head to the new node
        new_node.next = self.head  # Set the new node at the beginning
        self.head = new_node  # Update the head to the new node

    def delete(self, key):
        current = self.head
        while current:
            if current.data == key:
                if current.prev:  # If not the first node
                    current.prev.next = current.next
                if current.next:  # If not the last node
                    current.next.prev = current.prev
                if current == self.head:  # If it's the head node
                    self.head = current.next
                return
            current = current.next

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return current  # Return the node if found
            current = current.next
        return None  # Return None if not found

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> " if current.next else "")
            current = current.next
        print()


if __name__ == "__main__":
    sll = DoublyLinkedList()
    # Insert elements
    sll.prepend(1)
    sll.prepend(2)
    sll.prepend(3)
    sll.append(0)

    print("Linked List:", sll.display())  # Output: [0, 1, 2, 3]

    # Search for an element
    print("Search for 2:", sll.search(2))  # Output: True
    print("Search for 5:", sll.search(5))  # Output: False

    # Delete an element
    sll.delete_node(2)
    print("Linked List after deleting 2:", sll.display())  # Output: [0, 1, 3]
