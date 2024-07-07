class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def prepend(self, data):

        # adds data to the beginning of the list

        # [new data] + [original head]-[b]-[c]-[d]  -> [new data]-[original head]-[b]-[c]-[d]  we effectively appended
        # the new value to the head of the list

        new_node: Node = Node(data)  # initialize a new Node() with the desired data
        new_node.next = self.head  # set the next node to be the original head value
        self.head = new_node  # now the head of the list of Nodes becomes the new desired value we wished to append.

    def append(self, data):

        # adds data to the end of the list

        new_node: Node = Node(data)  # initialize a new Node() with the desired data
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_node(self, key):
        temp = self.head

        # If the head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        # Search for the key to be deleted, keep track of the previous node
        prev = None
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # If the key was not present in the linked list
        if temp == None:
            return

        # Unlink the node from the linked list
        prev.next = temp.next
        temp = None

    def search(self, key):
        current = self.head
        while current is not None:
            if current.data == key:
                return True
            current = current.next
        return False

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements


if __name__ == "__main__":
    sll = SinglyLinkedList()
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
