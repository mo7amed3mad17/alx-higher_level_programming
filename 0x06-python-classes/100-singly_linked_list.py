#!/usr/bin/python3
""" Node in a Singly Linked List Class."""


class Node:
    """ Node in SLL."""

    def __init__(self, data, next_node=None):
        """Init new Node
        Args:
        data (int): data
        next_node (Node): node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter of data."""
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter of next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ The SLL."""

    def __init__(self):
        """Init SLL."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SLL.
        insert into the list at the correct
        ordered numerical position.
        Args:
            value (Node): The new Node
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SLL."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
