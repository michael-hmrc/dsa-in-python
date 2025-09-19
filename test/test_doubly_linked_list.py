import pytest

from linked_lists.doubly_linked_list import (
    DoublyLinkedList,
    Node,
)  # Import your classes


# Test cases for the DoublyLinkedList class
def test_append():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)

    assert dll.head.data == 1
    assert dll.head.next.data == 2
    assert dll.head.next.next.data == 3
    assert dll.head.next.next.next is None


def test_prepend():
    dll = DoublyLinkedList()
    dll.prepend(3)
    dll.prepend(2)
    dll.prepend(1)

    assert dll.head.data == 1
    assert dll.head.next.data == 2
    assert dll.head.next.next.data == 3
    assert dll.head.next.next.next is None


def test_delete():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)

    dll.delete(2)

    assert dll.head.data == 1
    assert dll.head.next.data == 3
    assert dll.head.next.prev == dll.head
    assert dll.head.next.next is None


def test_search():
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)

    found_node = dll.search(2)
    assert found_node is not None
    assert found_node.data == 2

    not_found_node = dll.search(4)
    assert not_found_node is None


def test_display(capsys):
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)

    dll.display()

    captured = capsys.readouterr()
    assert captured.out == "1 <-> 2 <-> 3\n"


# If you want to run tests from the command line using pytest
if __name__ == "__main__":
    pytest.main()
