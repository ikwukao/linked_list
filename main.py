"""
Linked List Implementation

A simple implementation of a singly linked list using Object-Oriented
Programming (OOP) principles.

The linked list supports:

- Adding elements to the end of the list
- Removing elements from the list
- Checking whether the list is empty
- Tracking the number of stored elements

This project demonstrates:
- Nested classes
- Dynamic data structures
- Node-based memory organization
- Traversal algorithms
- Basic linked list operations

Created as part of a Python data structures learning project.
"""


# =========================================================
# LINKED LIST IMPLEMENTATION
# =========================================================


class LinkedList:
    """
    A singly linked list implementation.

    The list consists of Node objects connected through
    references to the next node in the sequence.

    Attributes:
        head (Node | None):
            Reference to the first node in the list.

        length (int):
            Number of elements currently stored in the list.
    """

    class Node:
        """
        Represents a single node within the linked list.

        Attributes:
            element:
                The value stored in the node.

            next (Node | None):
                Reference to the next node in the list.
        """

        def __init__(self, element):
            """
            Create a new node.

            Args:
                element:
                    The value to store in the node.
            """
            self.element = element
            self.next = None

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.length = 0
        self.head = None

    def is_empty(self):
        """
        Check whether the linked list contains any elements.

        Returns:
            bool:
                True if the list is empty, otherwise False.
        """
        return self.length == 0

    def add(self, element):
        """
        Add an element to the end of the linked list.

        Args:
            element:
                The value to add to the list.
        """
        # Create a new node containing the element.
        node = self.Node(element)

        # If the list is empty, the new node becomes the head.
        if self.is_empty():
            self.head = node

        else:
            # Traverse to the last node.
            current_node = self.head

            while current_node.next is not None:
                current_node = current_node.next

            # Attach the new node to the end of the list.
            current_node.next = node

        # Update list size.
        self.length += 1

    def remove(self, element):
        """
        Remove the first occurrence of an element from the list.

        Args:
            element:
                The value to remove.
        """
        previous_node = None
        current_node = self.head

        # Search for the target element.
        while current_node is not None and current_node.element != element:
            previous_node = current_node
            current_node = current_node.next

        # Element not found.
        if current_node is None:
            return

        # Element found somewhere after the head.
        elif previous_node is not None:
            previous_node.next = current_node.next

        # Element found at the head.
        else:
            self.head = current_node.next

        # Update list size.
        self.length -= 1


# =========================================================
# APPLICATION ENTRY POINT
# =========================================================

# Create an empty linked list.
my_list = LinkedList()

# Verify that the list starts empty.
print(my_list.is_empty())

# Add elements to the list.
my_list.add(1)
my_list.add(2)

# Verify that the list now contains data.
print(my_list.is_empty())

# Display the number of stored elements.
print(my_list.length)

# Remove an element from the list.
my_list.remove(1)

# Display the updated number of elements.
print(my_list.length)
